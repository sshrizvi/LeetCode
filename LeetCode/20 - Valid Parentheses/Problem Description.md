# 20 - Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input ***string is valid*** if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

***Example 1:***
Input: s = `"()"`
Output: true

***Example 2:***
Input: s = `"()[]{}"`
Output: true

***Example 3:***
Input: s = `"(]"`
Output: false
 
Constraints:

1. 1 <= `s.length` <= 104
2. `s` consists of parentheses only `'()[]{}'`.

---

## Solutions

### My Solution (Syed Shujaat Haider)

> To be honest I am not able to solve the problem. I checked the solutions, read the algorithms and then tried to code this.

![My Solution](https://github.com/sshrizvi/LeetCode/assets/89008579/8175a75c-4878-4812-a162-4f3f0a453cb8)

### Optimized Solution

> To read in detail, visit [Optimized Solution BY m_sripada](https://leetcode.com/problems/valid-parentheses/solutions/4499805/easy-and-explained/)

```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or stack.pop() != char:
                return False
        return not stack
```
