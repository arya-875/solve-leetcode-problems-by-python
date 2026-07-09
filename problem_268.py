def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return(i)
