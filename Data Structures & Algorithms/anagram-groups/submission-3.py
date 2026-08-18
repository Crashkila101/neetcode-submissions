class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
                # a = 80 -> 0, 80 - 80
                # b = 81 -> 1, 81 - 80
            res[tuple(count)].append(s)
        
        return list(res.values())
        # res = {}

        # for s in strs:
        #     sorted_s = sorted(s)
        #     sorted_string = ''.join(sorted_s)
        #     if sorted_string not in res:
        #         res[sorted_string] = [s]
        #     else:
        #         res[sorted_string].append(s)
        
        # return list(res.values())