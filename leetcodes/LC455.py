## This is Leetcode problem #455: Assign Cookies

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child

Solution().findContentChildren([1,2,1], [1,3,4])

