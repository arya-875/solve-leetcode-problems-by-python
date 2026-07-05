def plusOne(digits: List[int]) -> List[int]:
    num = int("".join(map(str,digits)))
    return[int(new_num) for new_num in str(num + 1)]
