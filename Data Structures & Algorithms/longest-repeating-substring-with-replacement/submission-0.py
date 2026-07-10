class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        i = 0
        j = 1
        ss = set(s)
        ml = 1
        count = {}

        for ch in ss:
            count[ch] = 0

        count[s[0]] += 1

        while j < len(s):
            count[s[j]] += 1

            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1

            ml = max(ml, j - i + 1)
            j += 1

        return ml