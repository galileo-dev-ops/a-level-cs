## This is Leetcode #4 - Median of Two Sorted Arrays
### https://leetcode.com/problems/median-of-two-sorted-arrays/

import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        return statistics.median(nums1)

Solution.findMedianSortedArrays(Solution, [1,3,5], [2])