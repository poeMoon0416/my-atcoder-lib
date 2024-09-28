# 切り上げ除算
# 絶対値の切り下げ/切り上げを反転する
def div_ceil(num, div):
    return -(-num//div)