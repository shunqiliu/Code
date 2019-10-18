'''
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
'''
My way:
Double pointer, p1 to 0, p2 to non-0.
First, p1 should be 0
when p2 find non zero, change the value of p1 and p2.
then p1+=1
if p2<p1:
p2=p1

The code are below
'''
nums=[0,1,0,3,12]
p1=0
p2=0
while p1<len(nums) and p2<len(nums):
    if nums[p1]!=0:
        p1+=1
    else:
        if p2<p1:
           p2=p1
           if nums[p2]!=0:
              nums[p1]=nums[p2]
              nums[p2]=0
           p2+=1