# 01. 인접 행렬 (adjacency matrix) 구현하기

class AdjacencyMatrix:
    def __init__(self, num_vertex, num_edge):
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.adjacency_matrix = list()
        for _ in range(self.num_vertex):
            temp_list = list()
            for _ in range(self.num_vertex):
                temp_list.append(0)
            self.adjacency_matrix.append(temp_list)
    
    def add_edge(self, start_vertex, end_vertex, weight):
        self.adjacency_matrix[start_vertex][end_vertex] = weight
    
    def matrix_display(self):
        for row_idx in range(self.num_vertex):
            print(*self.adjacency_matrix[row_idx])

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_vertex, num_edge = tuple(map(int, input().split()))
        temp_adjacency_matrix = AdjacencyMatrix(num_vertex, num_edge)

        for _ in range(num_edge):
            start_vertex, end_vertex, weight = tuple(map(int, input().split()))
            temp_adjacency_matrix.add_edge(start_vertex, end_vertex, weight)

        temp_adjacency_matrix.matrix_display()

if __name__ == "__main__":
    main()