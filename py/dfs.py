"""
# 深さ優先探索(再帰) O(V+E)
# 根からの距離を求める
# 呼び出し側でdist = [INF]*N, dist[root] = 0
def dfs(frm):
    for to in G[frm]:
        if dist[to] < INF:
            continue
        dist[to] = dist[frm]+1
        dfs(to)
"""

# 深さ優先探索(行きがけのみ/スタック) O(V+E)
# 根からの距離を求める
# 呼び出し側でdist = [INF]*N, dist[root] = 0
def dfs(start):
    st = [start]
    while st:
        frm = st.pop()
        for to in G[frm]:
            if dist[to] < INF:
                continue
            # 行きがけ処理
            dist[to] = dist[frm]+1
            st.append(to)

# 深さ優先探索(行きがけ帰りがけ両対応/スタック) O(V+E)
# 根からの距離を求める
# 呼び出し側でdist = [INF]*N, dist[root] = 0
def dfs(start):
    # 帰りがけ用頂点と行きがけ用頂点を用意する
    st = [~start, start]
    while st:
        frm = st.pop()
        if frm >= 0:
            # 行きがけ処理
            for to in G[frm]:
                if dist[to] < INF:
                    continue
                dist[to] = dist[frm]+1
                st.append(~to)
                st.append(to)
        else:
            # 帰りがけ処理
            frm = ~frm
            # ここに具体的な帰りがけ処理(再帰の戻り値でやるようなやつ)