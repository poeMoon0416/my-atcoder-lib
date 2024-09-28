# しゃくとり法 O(N)
# l], (r
def two_pointers(src):
    n = len(src)
    r = n-1
    for l in range(n):
        # 右の追い越し防止
        while r > l and "ここにrを進める条件":
            r -= 1
        # 左の追い越し修正
        if l > r:
            r = l
        # ここにメインの処理