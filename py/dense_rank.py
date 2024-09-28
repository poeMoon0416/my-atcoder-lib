# 座標圧縮 O(N)
# 10 10 12 24 -> 0 0 1 2 (rankだと0 0 2 3)
def dense_rank(src):
    # srcの重複を除いてソートして値と順位の対応を得る
    d = {v:i for i, v in enumerate(sorted(set(src)))}
    ret = [d[si] for si in src]
    return ret