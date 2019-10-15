'''
88. Merge Sorted Array

Share
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

'''
My way:

A typical pointer problem
set 3 pointers:
1.pointer point to the last value of num1
2.pointer point to the last value of num1
3.pointer point to the last value of num2

compare 2 value on p2 and p3, save the larger value by p1

The code are below
'''
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

a = m - 1
b = n - 1
c = m + n -1
while(b >= 0):
    if a >= 0 and nums1[a] >= nums2[b]:
        nums1[c] = nums1[a]
        a -= 1
    else:
        nums1[c] = nums2[b]
        b -= 1
    c -= 1
print(nums1)