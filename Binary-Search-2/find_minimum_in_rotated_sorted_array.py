"""## Problem 1: (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""
"""We are finding the min by considering the unsorted side has the minimum so we are using the binary search"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low <= high :
            if nums[low] <= nums[high]:
                return nums[low]
            mid = low +(high-low)//2
            if (mid==0 or nums[mid] <nums[mid-1]) and (mid==len(nums)-1 or nums[mid]<nums[mid+1]):
                return nums[mid]
            elif nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid-1


