import sys

from heapq import heappop, heappush

input = sys.stdin.readline

def dejkstra(start, n, graph):
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[start] = 0
    parents = [-1] * (n+1)

    pq = [(0, start)]

    while pq:
        d, u = heappop(pq)

        if d > dist[u]:
            continue

        for w, v in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parents[v] = u
                heappush(pq, (dist[v], v))

    return dist, parents

def find_path(parents, n):
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = parents[cur]

    path.reverse()
    return path



def main():
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b, w = map(int, input().strip().split())
        graph[a].append((w, b))
        graph[b].append((w, a))

    dist, parents = dejkstra(1, n, graph)

    if dist[n] == float("inf") or parents[n] == -1:
        print('-1')
        return

    path = find_path(parents, n)
    print(*path, sep=' ')



if __name__ == '__main__':
    main()