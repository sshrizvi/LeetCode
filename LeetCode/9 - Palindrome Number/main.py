class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = 0
        n = x
        while(x > 0):
            r = x % 10
            p = p * 10 + r
            x = x // 10
        if (p == n):
            return True
        else:
            return False