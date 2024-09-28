# 試し割り法 O(√N)
# Nを素因数分解
"""
N = 10^16でO(10^8)でも424msなので, 実際はみかけより早い
N = 10^18でO(10^9)だと3009ms
N = 10^17だと1048msなので, この辺が限界
"""
def prime_factors(src):
    # pf = {素因数p : 指数e}
    pf = defaultdict(int)
    now = src
    i = 2
    # src = i*j のときjがiより大きいなら既出なので√srcまで確認
    while i*i <= src:
        # 割り切れるなら割れるだけ割る
        while now%i == 0:
            now //= i
            pf[i] += 1
        i += 1
    # それ以上分解できない残ったものを素因数に加える
    if now > 1:
        pf[now] += 1
    return pf