from collections import defaultdict
from  graphlib import TopologicalSorter, CycleError

bad = []
# def topologicalSortUtil(v, adj, visited, stack):
#     # Mark the current node as visited
#     visited[v] = True

#     # Recur for all adjacent vertices
#     for i in adj[v]:
#         if not visited[i]:
#             topologicalSortUtil(i, adj, visited, stack)

#     # Push current vertex to stack which stores the result
#     stack.append(v)


# # Function to perform Topological Sort
# def topologicalSort(adj, V):
#     # Stack to store the result
#     stack = []

#     visited = [False] * V

#     # Call the recursive helper function to store
#     # Topological Sort starting from all vertices one by
#     # one
#     for i in range(V):
#         if not visited[i]:
#             topologicalSortUtil(i, adj, visited, stack)

#     # Print contents of stack
#     print("Topological sorting of the graph:", end=" ")
#     while stack:
#         print(stack.pop(), end=" ")
def checkUpdate(rules, update):
    inc = 0
    while inc < len(update):
        if inc+1 < len(update):
            if not checkRules(update[inc], update[inc+1], rules):
                bad.append(update)
                return False
        inc = inc +1
    return True

def checkRules(x , y, rules):
    filRules = [subinput for subinput in rules if x in subinput]
    for i in filRules:
        if y == i[0]:
            return False
            
    
    return True

def checkBadUpdates(rules, badupdate):
    ts = TopologicalSorter(dict.fromkeys(badupdate, ()))
    used = set(badupdate)
    for a, b in rules:
        if used >= {a, b}:
            ts.add(a, b)

    

    try:
        ts.prepare()
    except CycleError:
        pass
    
    result = []
    while ts.is_active():
        for node in ts.get_ready():
            used.remove(node)
            result.append(node)
            ts.done(node)
    if used:
        result+= sorted(used)

    return result
    


if __name__ == "__main__":

    input = []
    input2 = []
    graph = defaultdict(list) 
    with open("input.txt", 'r') as file:
        for line in file.readlines():
            input.append([int(s) for s in line.strip().split('|')])

    with open("input2.txt", 'r') as file: 
        for line in file.readlines():
            input2.append([int(s) for s in line.strip().split(',')])

    total = 0

    for x in input2:
        if(checkUpdate(input , x)):
            middle = len(x)//2
            total = total + x[middle]
    
    print("Part1: " + str(total))
    total = 0
    for b in bad:
        good = checkBadUpdates(input, b)
        middle = len(good)//2
        total = total + good[middle]
    print("Part2: " + str(total))
    
    