class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s.lower() :
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                st += i
        return st==st[::-1]