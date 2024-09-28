# 3*3のグリッド(要素数9の配列)の縦横斜めがそろっているか判定(oxゲーム)
def judge_line(ox):
    ret = "_"
    for i in range(3):
        # 横一列
        if ox[i*3] == "o" and ox[i*3+1] == "o" and ox[i*3+2] == "o":
            ret = "o"
            break
        if ox[i*3] == "x" and ox[i*3+1] == "x" and ox[i*3+2] == "x":
            ret = "x"
            break
        # 縦一列
        if ox[i] == "o" and ox[i+3] == "o" and ox[i+6] == "o":
            ret = "o"
            break
        if ox[i] == "x" and ox[i+3] == "x" and ox[i+6] == "x":
            ret = "x"
            break
    # 斜め(\, /)
    if ox[0] == "o" and ox[4] == "o" and ox[8] == "o":
        ret = "o"
    if ox[0] == "x" and ox[4] == "x" and ox[8] == "x":
        ret = "x"
    if ox[2] == "o" and ox[4] == "o" and ox[6] == "o":
        ret = "o"
    if ox[2] == "x" and ox[4] == "x" and ox[6] == "x":
        ret = "x"
    return ret