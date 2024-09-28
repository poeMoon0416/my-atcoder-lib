# エラトステネスの篩 O(NloglogN)
# N未満の素数列挙
"""
素数の倍数の削除について, N/2+N/3+N/5... = N(1/2+1/3+1/5...)
N未満の素数の逆数和はloglogNになるらしいので, O(NloglogN)
O(NloglogN)がTLEするほど大きな結果をコードに埋め込むことはできない。
TLEしない10^6以下の素数列挙でもテキストのサイズが600kBほどになってしまうため。
"""
def eratosthenes_sieve(lim):
    primes = set(range(3, lim, 2))
    primes.add(2)
    # iが素数か判定(奇数だけ見ていく)
    for i in range(3, lim, 2):
        if i in primes:
            # 素数iの倍数を削除
            for j in range(i*2, lim, i):
                primes.discard(j)
    return primes