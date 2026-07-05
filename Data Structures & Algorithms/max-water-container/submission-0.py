class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        i = 0
        j = len(heights)-1
        while i<j :
            b = min(heights[i],heights[j])
            l = j-i
            ma = max(ma,l*b)
            if heights[i]==b :
                i+=1
            else :
                j-=1
        return ma