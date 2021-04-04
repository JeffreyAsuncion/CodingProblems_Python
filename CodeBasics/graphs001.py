class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                # one value already exists. append to list
                self.graph_dict[start].append(end)
            else:
                # insert into dict
                self.graph_dict[start] = [end]
        print("Graph dict: ",self.graph_dict)
    
    def get_paths(self, start, end, path=[]):   # add path for recursion
        # we are going to use recursion
        path = path + [start]
        # we need to think about the simplest case first
        # base case : we are there already
        if start == end:
            return [path]
        # base case : there is no path or edge
        if start not in self.graph_dict:
            return []

        # now recursion
        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                # get the possible paths from this destiation to next
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths


    def get_shortest_path(self, start, end, path=[]):
        # we are going to use recursion
        path = path + [start]
        # we need to think about the simplest case first
        # base case : we are there already
        if start == end:
            return path
        # base case no paths
        if start not in self.graph_dict:
            return None

        # now recursion
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                # get the shortest paths from this destiation to next
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbia", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    # this is the form we are going to transform the routes (set)
    # d = {
    #     "Mumbai" : ["Paris", "Dubai"],
    #     "Paris" : ["Dubai", "New York"]
    # }


    # 1. find all paths from Mumbai to Toronto
    start = "Mumbai"
    end = "Toronto"
    print(f"paths between {start} and {end} : ", route_graph.get_paths(start, end))

    print("*"* 20)

    #2 find the shortes path (minimum stops)
    start = "Paris"
    end = "New York"
    print(f"shortest path between {start} and {end} : ", route_graph.get_shortest_path(start, end))