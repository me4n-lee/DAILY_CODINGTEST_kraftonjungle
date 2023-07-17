""" 
https://www.acmicpc.net/problem/2606<br/>
바이러스<br/>
2606
"""



import sys
from collections import deque
input = sys.stdin.readline

computers = int(input())
connect = int(input())
egdes = [[] for _ in range(computers + 1)]
visited = [False] * (computers + 1)
for _ in range(connect):
    start, end = map(int, input().split())
    egdes[start].append(end)
    egdes[end].append(start)
    
visited[1] = True

def bfs(graph, visited):
    # 시작 노드를 큐에 삽입
    count = 0
    dqueue = deque([1])
    # 큐가 빌 때까지 반복
    while dqueue:
        now_node = dqueue.popleft()
        for node in graph[now_node]:
            # 연결된 노드가 아직 방문되지 않았으면 방문하고 큐에 삽입
            if not visited[node]:
                count += 1
                visited[node] = True
                dqueue.append(node)
    return count


count = 0
count = bfs(egdes, visited)
print(count)