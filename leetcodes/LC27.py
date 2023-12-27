## This is Leetcode #27 - Remove Element
### https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
            global k
            k = 0
            for j in range(len(nums)):
                if nums[j] != "":
                    k = k + 1
        return nums
    