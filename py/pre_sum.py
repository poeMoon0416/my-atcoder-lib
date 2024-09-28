# 累積和 O(N)
# imos法で使う場合は[l, r)のlに+v, rに-vして累積和で復元
# 区間和の取得をO(1)で行える
def pre_sum(src):
    n = len(src)+1
    pre_sum = [0]*n
    for i in range(1, n):
        pre_sum[i] = pre_sum[i-1]+src[i-1]
    return pre_sum