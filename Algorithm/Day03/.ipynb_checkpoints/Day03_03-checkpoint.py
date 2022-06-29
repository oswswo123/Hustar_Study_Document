# 03. BFS (방향성 그래프)

import collections

class AdjacencyList:
    def __init__(self, num_vertex, num_edge):
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.adjacency_list = [list() for _ in range(self.num_vertex)]
    
    def add_edge(self, first_vertex, second_vertex):
        self.adjacency_list[first_vertex].append(second_vertex)
    
    def list_sorting(self):
        for row_idx in range(self.num_vertex):
            self.adjacency_list[row_idx] = sorted(self.adjacency_list[row_idx])
    
    def list_display(self):
        for row_idx in range(self.num_vertex):
            print(*self.adjacency_list[row_idx])
    
    def bfs(self, start_vertex):
        INF = 999999
        queue = collections.deque(list())
        output_list = list()
        
        dist_list = [INF for _ in range(self.num_vertex)]
        dist_list[start_vertex] = 0
        queue.append(start_vertex)
        while bool(queue):
            now_visit = queue.popleft()
            output_list.append(now_visit)
            for adjacency_vertex in self.adjacency_list[now_visit]:
                if dist_list[adjacency_vertex] == INF:
                    queue.append(adjacency_vertex)
                    dist_list[adjacency_vertex] = dist_list[now_visit] + 1        
        print(*output_list)
        
        
def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_vertex, num_edge = tuple(map(int, input().split()))
        temp_adjacency_list = AdjacencyList(num_vertex, num_edge)
    
        for _ in range(num_edge):
            first_vertex, second_vertex = tuple(map(int, input().split()))
            temp_adjacency_list.add_edge(first_vertex, second_vertex)

        temp_adjacency_list.list_sorting()
        temp_adjacency_list.bfs(0)

if __name__ == "__main__":
    main()