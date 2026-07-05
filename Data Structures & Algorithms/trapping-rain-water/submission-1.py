class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lm = 0
        rm = 0
        w = 0
        while l < r:
            lm = max(lm, height[l])
            rm = max(rm, height[r])
            if lm < rm:
                w += lm - height[l]
                l += 1
            else:
                w += rm - height[r]
                r -= 1
        return w