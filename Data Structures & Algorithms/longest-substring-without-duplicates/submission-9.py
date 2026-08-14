class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen = set()
        # l = 0
        # best = 0
        # for i in range(len(s)):
        #     while s[i] in seen:
        #         seen.remove(s[l])
        #         l+=1
        #     seen.add(s[i])
        #     best = max(i - l + 1, best)
        # return best

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
        