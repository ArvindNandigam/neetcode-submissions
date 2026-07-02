class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        l = [[] for _ in range(max(a.values()) + 1)]

        for i in a:
            l[a[i]].append(i)

        ans = []

        for freq in range(len(l) - 1, 0, -1):
            for num in l[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans