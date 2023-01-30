from queue import PriorityQueue

h, w, k = map(int, input().split())
map_ = [list(input()) for _ in range(h)]

start = None
for i in range(h):
    for j in range(w):
        if map_[i][j] == "N":
            start = (i, j)
            break
    if start:
        break


dist = [[float("inf")] * w for _ in range(h)]
dist[start[0]][start[1]] = 0
q = PriorityQueue()
q.put((0, start[0], start[1]))
dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]
while not q.empty():
    d, x, y = q.get()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if map_[nx][ny] != "#" and dist[nx][ny] > d + 1:
                dist[nx][ny] = d + 1
                q.put((dist[nx][ny], nx, ny))

min_dist = min(dist, key=lambda x: min(x))
min_dist = min(min_dist)
result = []
for i in range(h):
    for j in range(w):
        if dist[i][j] == min_dist and map_[i][j] != "N":
            result.append(int(map_[i][j]))
print(len(result))
for r in sorted(result):
    print(r)
