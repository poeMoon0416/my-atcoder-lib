# クラスカル法 O(ElogE)
"""
MST(最小全域木)のコスト総和を求める。
辺をコストの昇順にソートして貪欲にとる。
MSTは最小コストで全頂点を連結にすればよいので, すでに連結ならとらない。
"""
def kruskal():
    UF = DSU(N)
    ret = 0
    for c, u, v in sorted(E):
        if not UF.same(u, v):
            UF.merge(u, v)
            ret += c
    # MSTが作れない場合
    if UF.size(0) < N:
        ret = INF
    return ret