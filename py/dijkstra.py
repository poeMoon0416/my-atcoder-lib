# ダイクストラ法 O((V+E)logV)
"""
単一始点最短経路(1つの頂点からすべての頂点までの最短経路)を求める。
ダイクストラ法のベースは幅優先探索。
最短距離が未確定の頂点のうち,
暫定最短距離が最短の頂点はその時点で距離が確定する。
その頂点は回り道したら必ず距離が暫定最短距離より大きくなるため。
負のコストが存在すると回り道した方がコストが小さくなる可能性があるため,
ダイクストラ法が使えない。
"""
def dijkstra(start):
    # 各頂点の始点からの距離
    dist = [INF]*N
    dist[start] = 0
    # 経路復元用の各頂点の最短経路における前の要素
    prev = [-1]*N
    # visited[i]: 最短距離確定済みか
    visited = [False]*N
    # (距離, 頂点)の優先度付きキュー
    pq = [(0, start)]
    
    while pq:
        # 暫定距離最短の頂点の距離を確定してたどる
        frm = heappop(pq)[1]
        if visited[frm]:
           continue
        visited[frm] = True
        for frm_to_dist, to in G[frm]:
            # 暫定最短距離と前の頂点の更新
            if dist[frm]+frm_to_dist < dist[to]:
                dist[to] = dist[frm]+frm_to_dist
                prev[to] = frm
                heappush(pq, (dist[to], to))
    
    # 最短経路を終点から遡って復元
    # デフォルトの終点: N-1
    path = [N-1]
    frm = prev[path[0]]
    while frm > -1:
        path.append(frm)
        frm = prev[frm]
    # frm->to方向に直す
    path = path[::-1]
    
    # 始点から終点までの最短経路, 始点からの最短距離
    # print(*path)
    return dist