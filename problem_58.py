def lengthOfLastWord(s: str) -> int:
    letters = []
    s = s.strip()
    for i in s[::-1]:
        if i != " ":
            letters.append(i)
        if i == " ":
            break
    letters = letters[::-1]
    ans = len("".join(map(str,letters)))
    return(ans)
