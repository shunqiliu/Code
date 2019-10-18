'''
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

'''
My way:(cannot be solved by myself)

Divide the intr to 3 part:
1. right value is less than the newi[0]
2. merged interval
3. left value is larger than the newi[1]

key point: 
1. Try to use while loop, because while the intr length is 1, the i in while is add to 1, but in for loop, the i will be 0, which causes the problem of dividing
2. Using the min and max to iterate the merge interval, instead of using multiple if...else

TRY IT AGAIN, TRUST YOUR SELF!!!!

The code are below
'''
intr=[[1,2],[3,5],[6,7],[8,10],[12,16]]
newi=[4,8]
new=[]
if not intr:
    print [newi]
i=0
while i<len(intr) and intr[i][1]<newi[0]:
    new.append(intr[i])
    i+=1
    cur=newi
    for j in range(i,len(intr)):
        if cur[1]>=intr[j][0]:
            cur=[min(cur[0],intr[j][0]),max(cur[1],intr[j][1])]
        else:
            new.append(cur)
            cur=intr[j]
new.append(cur)
print(new)
