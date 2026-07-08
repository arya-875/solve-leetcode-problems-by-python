def isPalindrome(s: str) -> bool:
    letters = 'abcdefghijklmnopqrstuvwxyz0987654321'
    s = s.lower()
    s = [i for i in s if i in letters]
    s = ''.join(map(str,s))
    if s == s[::-1]:
        return(True)
    return(False)
