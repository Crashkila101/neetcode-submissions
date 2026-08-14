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

        seen = set()
        l = 0
        res = 0

        for i in range(len(s)):
            if s[i] in seen:
                while s[l] != s[i]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                seen.add(s[i])
                res = max(res, i - l + 1)
        return res
        