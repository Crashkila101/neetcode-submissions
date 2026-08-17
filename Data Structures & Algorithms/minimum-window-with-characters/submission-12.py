class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        l = 0
        countT  = {}
        countS = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        have = 0
        need = len(countT)
        res = [-1, -1]
        currLength = math.inf

         
        for r, char in enumerate(s):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < currLength:
                    res = [l, r]
                    currLength = min(currLength, r - l + 1)
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]+1] if currLength != math.inf else ""