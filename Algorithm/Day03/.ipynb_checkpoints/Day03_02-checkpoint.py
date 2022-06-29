# 02. 인접 리스트 (adjacency list) 구현하기

class AdjacencyList:
    def __init__(self, num_vertex, num_edge):
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.adjacency_list = [list() for _ in range(self.num_vertex)]
    
    def add_edge(self, first_vertex, second_vertex):
        self.adjacency_list[first_vertex].append(second_vertex)
        self.adjacency_list[second_vertex].append(first_vertex)
    
    def list_sorting(self):
        for row_idx in range(self.num_vertex):
            self.adjacency_list[row_idx] = sorted(self.adjacency_list[row_idx])
    
    def list_display(self):
        for row_idx in range(self.num_vertex):
            print(*self.adjacency_list[row_idx])

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_vertex, num_edge = tuple(map(int, input().split()))
        temp_adjacency_list = AdjacencyList(num_vertex, num_edge)

        for _ in range(num_edge):
            first_vertex, second_vertex = tuple(map(int, input().split()))
            temp_adjacency_list.add_edge(first_vertex, second_vertex)

        temp_adjacency_list.list_sorting()
        temp_adjacency_list.list_display()

if __name__ == "__main__":
    main()