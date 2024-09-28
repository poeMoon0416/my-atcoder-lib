# ワーシャル-フロイド法 O(V^3)
"""
全点対最短経路(すべての頂点からすべての頂点までの最短経路)を求める。
基本的に隣接行列でやるものとしている。
経由する頂点の候補を増やしていくDP。
これは回り道がどうとか考えないので, 負のコストが存在しても動作する。
"""
def warshall_floyd():
    for via in range(N):
        for frm in range(N):
            for to in range(N):
                G[frm][to] = min(G[frm][to], G[frm][via]+G[via][to])