#include <opencv2/opencv.hpp>
#include "hough_regression.h"

std::vector<cv::Point> regression_and_detection_points(cv::Mat inputimage, std::vector<cv::Vec4i> inputlines) {
	cv::Point slope_p1, slope_p2;
	std::vector<double> slopes;
	std::vector<cv::Vec4i> slope_lines;

	for (int i = 0; i < inputlines.size(); i++) {
		cv::Vec4i line = inputlines[i];
		slope_p1 = cv::Point(line[0], line[1]);
		slope_p2 = cv::Point(line[2], line[3]);
		double slope;
		if (slope_p2.x - slope_p1.x == 0) {
			// ���� ���� �� 0���� �������� ����
			slope = 500.0;
		}
		else {
			slope = (double)(slope_p2.y - slope_p1.y) / (double)(slope_p2.x - slope_p1.x);
		}

		double slope_threshold = 0.8;
		if (abs(slope) > slope_threshold) {
			// ���� 0.5 ������ ���� ���꿡�� ����
			slopes.push_back(slope);
			slope_lines.push_back(line);
		}
	}

	// ���Ⱑ ������ ����ȭ���� ��, ���Ⱑ ����� ������ ȭ���� ��
	// Why? cv���� y���� Ŀ���� �Ʒ��� ������ϱ�
	cv::Point sep_p1, sep_p2;
	double img_center = (double)(inputimage.cols / 2);
	std::vector<cv::Vec4i> sep_lines[2];
	for (int i = 0; i < slope_lines.size(); i++) {
		sep_p1 = cv::Point(slope_lines[i][0], slope_lines[i][1]);
		sep_p2 = cv::Point(slope_lines[i][2], slope_lines[i][3]);

		if (slopes[i] > 0 && sep_p1.x > img_center && sep_p2.x > img_center) {
			sep_lines[1].push_back(slope_lines[i]);
		}
		else if (slopes[i] < 0 && sep_p1.x < img_center && sep_p2.x < img_center) {
			sep_lines[0].push_back(slope_lines[i]);
		}
	}

	double left_m, right_m;
	cv::Point left_bias, right_bias;
	std::vector<cv::Point> detection_lanepoint(4);
	cv::Point reg_p1, reg_p2;
	cv::Vec4d regline[2];					// 0 : ����, 1 : ������
	std::vector<cv::Point> regline_points[2];	// 0 : ����, 1 : ������

	// ���� �� linear regression
	for (auto left_line : sep_lines[0]) {
		// ���� �� Point ��ǥ ����
		reg_p1 = cv::Point(left_line[0], left_line[1]);
		reg_p2 = cv::Point(left_line[2], left_line[3]);
		regline_points[0].push_back(reg_p1);
		regline_points[0].push_back(reg_p2);
	}
	if (regline_points[0].size() > 0) {
		// �־��� line data�� ������ fitting
		cv::fitLine(regline_points[0], regline[0], cv::DIST_L2, 0, 0.01, 0.01);

		left_m = regline[0][1] / regline[0][0];
		left_bias = cv::Point(regline[0][2], regline[0][3]);
	}

	// ������ �� linear regression
	for (auto right_line : sep_lines[1]) {
		// ������ �� Point ��ǥ ����
		reg_p1 = cv::Point(right_line[0], right_line[1]);
		reg_p2 = cv::Point(right_line[2], right_line[3]);
		regline_points[1].push_back(reg_p1);
		regline_points[1].push_back(reg_p2);
	}
	if (regline_points[1].size() > 0) {
		// �־��� line ddata�� ������ fitting
		cv::fitLine(regline_points[1], regline[1], cv::DIST_L2, 0, 0.01, 0.01);

		right_m = regline[1][1] / regline[1][0];
		right_bias = cv::Point(regline[1][2], regline[1][3]);
	}

	// y = m * (x - xb) + yb   ->   x = ((y - b) / m) + xb
	int low_y = inputimage.rows;
	int high_y = inputimage.rows * 0.6;

	double leftx1 = ((low_y - left_bias.y) / left_m) + left_bias.x;
	double leftx2 = ((high_y - left_bias.y) / left_m) + left_bias.x;
	double rightx1 = ((low_y - right_bias.y) / right_m) + right_bias.x;
	double rightx2 = ((high_y - right_bias.y) / right_m) + right_bias.x;

	detection_lanepoint[0] = cv::Point(leftx1, low_y);
	detection_lanepoint[1] = cv::Point(leftx2, high_y);
	detection_lanepoint[2] = cv::Point(rightx1, low_y);
	detection_lanepoint[3] = cv::Point(rightx2, high_y);

	return detection_lanepoint;
}