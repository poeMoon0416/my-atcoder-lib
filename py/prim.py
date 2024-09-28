# プリム法 O(ElogE)
"""
MST(最小全域木)のコスト総和を求める。
ダイクストラ法のように訪問済みの頂点に隣接する辺のうち,
コストが最小の辺からとって, その先の頂点を訪問済みにしていく。
どの頂点からスタートしてもok.
"""
def prim():
    ret = 0
    visited = {0}
    pq = []
    for c, to in G[0]:
        heappush(pq, (c, to))
    while len(visited) < N and len(pq) > 0:
        c, frm = heappop(pq)
        if frm in visited:
            continue
        ret += c
        visited.add(frm)
        for c, to in G[frm]:
            if to in visited:
                continue
            heappush(pq, (c, to))
    # MSTが作れない場合
    if len(visited) < N:
        ret = INF
    return ret