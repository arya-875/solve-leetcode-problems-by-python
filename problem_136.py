def singleNumber(nums: List[int]) -> int:
    if len(nums) == 1:
        return(int("".join(map(str,nums))))
    for i in nums:
        if nums.count(i) == 1:
            return(i)
