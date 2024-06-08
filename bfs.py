def bfs(graph,source):
    queue=[ source ]
    while len(queue) != 0:
        temp=queue.pop(0)
        print(temp)
        for i in graph[temp]:
            queue.append(i)


graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[],
}

bfs(graph,'a')