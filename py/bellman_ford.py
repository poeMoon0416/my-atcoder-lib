# ベルマンフォード法 O(VE)
"""
負の閉路がなければ再訪問は起きないので,
最短経路の経由頂点数の最大値はV-1個となる。
最短経路の部分経路が最短経路でなければ置き換えて短縮可能になってしまうので,
最短経路の部分経路は経由頂点数が自身未満の最短経路である。
それを利用して経由頂点数が0..V-1までの最短経路で動的計画法をするイメージのようだ。
負の閉路から到達可能かの判定については,
最初の1回で-INFとなる始点を求めて, 残りV-1回で影響を拾う。
"""
def bellman_ford(start):
    dist = [INF]*N
    dist[start] = 0
    # 最短経路を求める
    for _ in range(N-1):
        for dist_frm_to, frm, to in E:
            if dist[frm] < INF:
                dist[to] = min(dist[to], dist[frm]+dist_frm_to)
    # 負の閉路(の始点となる-INF)発見
    for dist_frm_to, frm, to in E:
        if dist[frm] < INF and dist[frm]+dist_frm_to < dist[to]:
            dist[to] = -INF
    # 負の閉路から到達可能か
    for _ in range(N-1):
        for dist_frm_to, frm, to in E:
            if dist[frm] == -INF:
                dist[to] = -INF
    return dist