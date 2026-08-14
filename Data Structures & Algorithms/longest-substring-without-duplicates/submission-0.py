class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        best = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            best = max(i - l + 1, best)
        return best
        