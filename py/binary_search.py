# 二分探索 O(logN)
"""
sより小さい最大値の位置を返す(挿入位置ではない)
同じ値が存在する場合は最も右の値の位置を返す
"""
def binary_search(s):
    # 半開区間[cl, op)
    cl, op = 0, N
    while abs(cl-op) > 1:
        m = (cl+op)//2
        if A[m] < s:
            cl = m
        else:
            op = m
        m = (cl+op)//2
        # print(cl, m, op)
    return cl