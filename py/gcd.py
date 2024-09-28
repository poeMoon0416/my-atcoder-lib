# ユークリッドの互除法 O(logN)
# 最大公約数(gcd)を求める
"""
gcdはaとbの約数の積集合
"""
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a%b != 0:
        a, b = b, a%b
    return b