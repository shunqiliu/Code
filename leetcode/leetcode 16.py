'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
'''
My way:
Double pointer

j point to i+1
k point to end

if cur == pre, continue

save all the sum, and compare with new one
output the optimal sum

U are not working out this problem, TRY AGAIN!!!!

The code are below
'''
nums=[-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
target=0
nums.sort()
closest_sum =float('inf')
for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    j = i+1; k = len(nums)-1
    while j < k:
       current_sum = nums[i] + nums[j] + nums[k]
       if abs(current_sum - target) < abs(closest_sum - target):
           closest_sum = current_sum  
       if current_sum < target:
           while j < k and nums[j] == nums[j+1]:
               j += 1
           j += 1 
       elif current_sum > target:
           while k > j and nums[k] == nums[k-1]:
              k -= 1
           k -= 1
       else:
           break
print(closest_sum)