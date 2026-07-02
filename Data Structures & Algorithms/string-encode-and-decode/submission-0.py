class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += f"{len(i)}#{i}"
        return s
    def decode(self, s: str) -> List[str]:
        a = ""
        ss = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                a += s[i]
                i += 1
            else:
                ss.append(s[i+1:i+1+int(a)])
                i = i + 1 + int(a)
                a = ""
        return ss