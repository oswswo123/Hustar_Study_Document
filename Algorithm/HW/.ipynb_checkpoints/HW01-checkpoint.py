# HW 01. "랜선" 웨어

import sys
sys.setrecursionlimit(1000000)

class AdjacencyList:
    def __init__(self, num_of_vertex, num_of_edge):
        self.num_of_vertex = num_of_vertex
        self.num_of_edge = num_of_edge
        self.adjacency_list = [list() for _ in range(num_of_vertex)]
    
    def add_edge(self, first_point, second_point):
        self.adjacency_list[first_point].append(second_point)
        self.adjacency_list[second_point].append(first_point)
    
    def list_sorting(self):
        for idx in range(self.num_of_vertex):
            self.adjacency_list[idx] = sorted(self.adjacency_list[idx])
    
    def list_display(self):
        for idx in range(self.num_of_vertex):
            print(*self.adjacency_list[idx])
    
    def dfs(self, start_vertex):
        self.visited_list = [False for _ in range(self.num_of_vertex)]
        self.output_list = list()
        
        self.visited_list[start_vertex] = True
        self.explore(start_vertex)

        return self.output_list
    
    def explore(self, vertex):
        self.visited_list[vertex] = True
        self.output_list.append(vertex)
        for adjacency_vertex in self.adjacency_list[vertex]:
            if self.visited_list[adjacency_vertex] == False:
                self.explore(adjacency_vertex)

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_of_vertex, num_of_edge, start_point = tuple(map(int, input().split()))
        temp_adjacency_list = AdjacencyList(num_of_vertex, num_of_edge)
        
        for _ in range(num_of_edge):
            first_point, second_point = tuple(map(int, input().split()))
            temp_adjacency_list.add_edge(first_point, second_point)
        
        temp_adjacency_list.list_sorting()
        print(num_of_vertex - len(temp_adjacency_list.dfs(start_point)))

if __name__ == "__main__":
    main()