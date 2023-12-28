## This is Leetcode #88 - Merge Sorted Array
## https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = j = 0

        while i < m + j and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()  # remove the last element
                j += 1
            else:
                i += 1
        while j < n:  # add remaining elements from nums2
            nums1[i] = nums2[j]
            i += 1
            j += 1
        return nums1

result = Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(result)