# 転置行列を求める
def transpose(src):
    ret = [[0]*H for _ in range(W)]
    for i in range(W):
        for j in range(H):
            ret[i][j] = src[j][i]
    return ret