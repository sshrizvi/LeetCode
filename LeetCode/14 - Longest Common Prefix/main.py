def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    first = strs[0]
    j = 1
    flag = 0
    while(flag == 0 and j <= len(first)):
        for i in range(1,len(strs)):
            if strs[i].startswith(first[:j]):
                pass
            else:
                flag = 1
                break
        else:
            prefix = first[:j]
            j = j + 1
        if flag == 1 and prefix == "":
            return prefix
    return prefix

strs = ["flowers","flow","flight"]
print(longestCommonPrefix(strs))