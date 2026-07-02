class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s :
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                st += i.lower()
        return st==st[::-1]