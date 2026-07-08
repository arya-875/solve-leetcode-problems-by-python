def addDigits(num: int) -> int:
    while num >= 10:
        num = sum(int(digits) for digits in str(num))
    return(num)
