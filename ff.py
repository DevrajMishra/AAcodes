class ff:
    def __init__(self,graph) -> None:
        self.graph = graph
        self.row = len(graph)
    
    def dfs(self,source,sink, parent):
        stack = [source]
        visited = [False] * self.row
        visited[source] = True
        while stack:
            u = stack.pop()
            print("u ",u)
            for idx,val in enumerate(self.graph[u]):
                if val > 0 and visited[idx] == False:
                    print(idx,val)
                    visited[idx] = True
                    stack.append(idx)
                    parent[idx] = u
                    print("visited: ",visited)
                    print("stack",stack)
                    print("parent",parent)
                    if idx == sink:
                        return True
        return False

    def ford(self,source,sink):
        parent = [-1] * self.row
        totalFlow = 0

        while self.dfs(source,sink,parent):
            flow = float("Inf")

            s = sink
            while s != source:
                flow = min(flow, self.graph[parent[s]][s])
                print("flow",flow)
                s = parent[s]
            totalFlow += flow

            a = sink
            while a != source:
                print(a,end="-")
                a = parent[a]
            print(source,"flow is :",flow)

            v = sink
            while v != source: #update the flow 
                u = parent[v]
                self.graph[v][u] += flow
                self.graph[u][v] -= flow
                v = parent[v]
        return totalFlow

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
 
g = ff(graph)
 
source = 0; sink = 5
  
print ("The maximum possible flow is ", g.ford(source, sink))