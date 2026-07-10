class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        ml = 0
        i = 0

        for j in range(len(s)):
            if s[j] in last_seen and last_seen[s[j]] >= i:
                i = last_seen[s[j]] + 1

            last_seen[s[j]] = j
            ml = max(ml, j - i + 1)

        return ml