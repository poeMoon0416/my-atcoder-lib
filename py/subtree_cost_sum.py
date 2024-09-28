# 自身を含む自身以下の部分木のコスト総和を求める
def subtree_cost_sum(start):
    st = [~start, start]
    while st:
        frm = st.pop()
        if frm >= 0:
            for to in G[frm]:
                if visited[to]:
                    continue
                visited[to] = True
                st.append(~to)
                st.append(to)
        else:
            frm = ~frm
            # 帰りがけ順に処理されるので自身と直下の子のみ足せばよい
            C_sum[frm] = C[frm]+sum([C_sum[to] for to in G[frm]])