# Day 03 - PJ 01. 최단 경로 구하기 (Dijkstra)

import collections
import heapq

INF = 999999

class AdjacencyList:
    global INF
    def __init__(self, num_vertex, num_edge):
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.adjacency_list = [list() for _ in range(self.num_vertex)]
    
    def add_edge(self, first_vertex, second_vertex, weight):
        self.adjacency_list[first_vertex].append((weight, second_vertex))
    
    def list_sorting(self):
        for row_idx in range(self.num_vertex):
            self.adjacency_list[row_idx] = sorted(self.adjacency_list[row_idx], key=lambda x:x[0])
    
    def list_display(self):
        for row_idx in range(self.num_vertex):
            print(*self.adjacency_list[row_idx])
    
    def dijkstra(self, start_vertex):
        self.distance_list = [INF for _ in range(self.num_vertex)]
        self.prev_vertex = [None for _ in range(self.num_vertex)]
        self.distance_list[start_vertex] = 0
        
        heap = list()        
        for idx in range(self.num_vertex):
            heapq.heappush(heap, (self.distance_list[idx], idx))
        
        while bool(heap):
            now_distance, now_visit = heapq.heappop(heap)
            for adj_distance, adjacency_vertex in self.adjacency_list[now_visit]:
                if self.distance_list[adjacency_vertex] > self.distance_list[now_visit] + adj_distance:
                    self.distance_list[adjacency_vertex] = self.distance_list[now_visit] + adj_distance
                    self.prev_vertex[adjacency_vertex] = now_visit
                    change_idx = [idx for idx, element in enumerate(heap) if element[1] == adjacency_vertex]
                    heap[change_idx[0]] = (self.distance_list[adjacency_vertex], adjacency_vertex)
                    heapq.heapify(heap)


def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_vertex, num_edge = tuple(map(int, input().split()))
        temp_adjacency_list = AdjacencyList(num_vertex, num_edge)
    
        for _ in range(num_edge):
            first_vertex, second_vertex, weight = tuple(map(int, input().split()))
            temp_adjacency_list.add_edge(first_vertex, second_vertex, weight)

        temp_adjacency_list.list_sorting()
        temp_adjacency_list.dijkstra(0)
        if temp_adjacency_list.distance_list[-1] == INF:
            print(-1)
        else:
            print(temp_adjacency_list.distance_list[-1])

if __name__ == "__main__":
    main()