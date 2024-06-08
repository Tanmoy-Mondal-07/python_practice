def dfs(graph,source):
    stack=[ source ]
    while len(stack) != 0:
        current=stack.pop()
        print(current)
        for neighbor in (graph[current]):
            stack.append(neighbor)

def recursive_dfs(graph,source):
    print(source)
    for i in graph[source]:
        recursive_dfs(graph,i)


graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[],
}

dfs(graph,'a')
print("recursive")
recursive_dfs(graph,'a')