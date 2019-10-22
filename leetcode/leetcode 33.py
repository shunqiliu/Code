'''
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
'''
My way:

When we see the O(logn), it must be binary search
so here the nums are half sorted, divided to 2 parts:
if the target is less than first element, target must be in the right part
elif the  target is larger than first element, target must be in the left part

Then apply the binary search in two part

The code are below
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if nums[0]==target:
            return 0
        if nums[-1]==target:
            return len(nums)-1
        if target>nums[0]:
            left=0
            right=len(nums)-1
            while left<right-1:
                mid=(left+right)//2
                if nums[mid]<nums[0]:
                    right=mid
                    mid=(left+right)//2
                else:
                    if nums[mid]<target:
                        left=mid
                        mid=(left+right)//2
                    elif nums[mid]>target:
                        right=mid
                        mid=(left+right)//2
                    else:
                        return mid
            return -1
        else:
            left=0
            right=len(nums)-1
            while left<right-1:
                mid=(left+right)//2
                if nums[mid]>nums[0]:
                    left=mid
                    mid=(left+right)//2
                else:
                    if nums[mid]<target:
                        left=mid
                        mid=(left+right)//2
                    elif nums[mid]>target:
                        right=mid
                        mid=(left+right)//2
                    else:
                        return mid
            return -1