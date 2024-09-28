# 幅優先探索 O(V+E)
# BFSごとにリセットする場合: in_visited = defaultdict(bool)
def bfs(start):
    q = deque([start])
    while q:
        frm = q.popleft()
        visited[frm] = True
        for to in G[frm]:
            if visited[to]:
                continue
            visited[to] = True
            q.append(to)