# bitDP O(4^N) (種類をNとすると(2^N)^2 = 2^(N*2) = 4^N)
"""
選ぶ/選ばないの組合せを表すビットを状態にとる動的計画法
全ての選択肢に対してありうる全ての状態からの遷移を求める
下記のNは組合せのビット数なので注意
"""
def bit_dp(src):
    # 元データの数を状態の数に圧縮する
    src = Counter(src)
    N = 2**len(src)
    dp = [0]*N
    # どれも選ばない場合が1通り
    dp[0] = 1
    for src_bits, cnt in src:
        # 逆順に更新すれば1次元配列でも二重に更新されない
        for frm_bits in range(N-1, -1, -1):
            # srcから1つ以上選ぶ遷移, 爆発しないようにMODをとる
            dp[frm_bits|src_bits] += (dp[frm_bits]*(2**cnt-1))%MOD
            dp[frm_bits|src_bits] %= MOD
    return dp