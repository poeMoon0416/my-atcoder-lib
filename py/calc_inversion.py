# バブルソートで転倒数を求める O(N^2)
def calc_inversion(src):
    N = len(src)
    inv = 0
    for i in range(1, N):
        for j in range(N-i):
            if src[j] > src[j+1]:
                src[j], src[j+1] = src[j+1], src[j]
                inv += 1
    return inv