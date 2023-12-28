## This is Leetcode #1531 - String Compression II
### https://leetcode.com/problems/string-compression-ii/

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        getLength = lambda x: 1 if x < 2 else 2 if x < 10 else 3 if x < 100 else 4
        def recur(i, k):
            if i < 0: return 0
            res = recur(i - 1, k - 1) if k else 9e9
            freq = 0
            for j in range(i, -1, -1):
                if s[i] == s[j]: freq += 1
                elif k == 0: return res
                else: k -= 1
                res = min(res, recur(j - 1, k) + getLength(freq))
            
            return res
        return recur(len(s) - 1, k)