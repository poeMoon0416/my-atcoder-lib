# 木の重心を求める
"""
直線とウニとその間の木で考えても重心での距離総和が最小で,
重心で木を分解したときの部分木の頂点数の最大値の最小値はN//2以下。
複数N//2より大きいtoが存在すると考えると頂点数がNを超えて矛盾するためtoはfrmに対して1つ。
頂点数でなくコストでも同様のことが成り立つ。
"""
def centroid(start):
    st = [start]
    while st:
        frm = st.pop()
        for to in G[frm]:
            if visited[to]:
                continue
            visited[to] = True
            if C_sum[to] > C_sum[0]//2:
                st.append(to)
    return frm