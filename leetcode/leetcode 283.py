'''
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

'''
My way:

Using pointer. When the pointer find 0, pop this value, if not 0, pointer+=1. Remenber the k times of pop
Then append k times zero

The code are below
'''
nums=[0,1,0,3,12]
p=0
k=0
nums.append(None)
while nums[p]!=None:
    if nums[p]==0:
        nums.pop(p)
        k+=1
    else:
         p+=1
nums.pop()
for i in range(k):
    nums.append(0)

print(nums)