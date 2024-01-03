# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

***Example 1:***
Input: strs = ["flower","flow","flight"]
Output: "fl"

***Example 2:***
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

***Constraints:***
1. 1 <= strs.length <= 200
2. 0 <= strs[i].length <= 200
3. strs[i] consists of only lowercase English letters.

---

## Solutions

### My Solution (Syed Shujaat Haider)
```
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
```

### Optimized Solution
```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return prefix
            prefix+=first[i]
        return prefix 
```