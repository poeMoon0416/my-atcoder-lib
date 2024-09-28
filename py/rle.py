# ランレングス圧縮 O(N)
def rle(src):
    return [(k, len(list(v))) for k, v in groupby(src)]