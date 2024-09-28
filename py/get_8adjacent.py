# 8隣接の取得
# "#"判定は呼び出し側
def get_8adjacent(frm):
    ret = []
    i, j = frm[0], frm[1]
    d = (-1, 0, 1)
    for di in d:
        ii = i+di
        for dj in d:
            jj = j+dj
            if ii == i and jj == j:
                continue
            if 0 <= ii < H and 0 <= jj < W:
                ret.append((ii, jj))
    return ret