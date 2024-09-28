# 4隣接の取得
# "#"判定は呼び出し側
def get_4adjacent(i, j):
    ret = []
    # 時計回り
    if 0 <= i-1 < H:
        ret.append((i-1, j))
    if 0 <= j+1 < W:
        ret.append((i, j+1))
    if 0 <= i+1 < H:
        ret.append((i+1, j))
    if 0 <= j-1 < W:
        ret.append((i, j-1))
    return ret