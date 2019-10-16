'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
My way:

Trible pointers: First sort the list.one pointer gives the sum of rest two variables, then it becomes to two sum problem, we using double pointer to solve it

Remind: because the result is a set, which means no repeat element, so we should jump the pointer when the besides values are same.

The code are below
'''

nums=[-1,0,3,2,4,15,-23,0,2,1,-2,-4,3]

nums.sort()
res = []
        
for i in range(len(nums)-2):
    if i==0 or nums[i]>nums[i-1]:
        p1=i+1
        p2=len(nums)-1
        while p1<p2:
            if (nums[p1]+nums[p2])==(-nums[i]):
                res.append([nums[i],nums[p1],nums[p2]])
                p1+=1
                p2-=1
                while p1 < p2 and nums[p1] == nums[p1-1]:
                    p1 +=1
                while p1 < p2 and nums[p2] == nums[p2+1]:
                    p2 -= 1
            elif nums[p1]+nums[p2]>-nums[i]:
                while p1 < p2:
                    p2-=1
                    if nums[p2] < nums[p2+1]: break
            else:
                while p1 < p2:
                    p1+=1
                    if nums[p1] > nums[p1-1]: break

print(res)