class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs :
            ab = "".join(sorted(i))
            if a.__contains__(ab) :
                a[ab].append(i)
            else :
                a[ab] = [i]
        return list(a.values())