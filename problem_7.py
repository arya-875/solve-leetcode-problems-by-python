def reverse(x: int) -> int:
    res = abs(x)
    res = int(str(res)[::-1])
    if x > 0:
        if (-res > (2 ** 31) - 1) or (-res < -2 ** 31):
            return(0)
    if x < 0:
        if (-res > (2 ** 31) - 1) or (-res < -2 ** 31):
            return(0)
    if str(x)[-1] == 0 and x < 0:
        return(int(str(-res)[1::]))
    if str(x)[-1] == 0:
        return(int(str(res)[1::]))
    if x < 0:
        return(-res)
    return(int(str(x)[::-1]))
