'''
Leetcode 6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''

'''
My way:

The regularity is that in different row, the next letter has the constant distance with last one. 
The constant distance has some pattern:
1. For the first and last row, the distance is only 1 value.
2. For the other rows, the distance is changed between 2 values, and each time changes once.

Based on the regularity above, the distance, here we use up to represent the upper distance and down to represent the down distance, are:
up=[0]+[ 2*i-1 for i in range(1,numRows+1)]
down=[2*i-1 for i in range(numRows-1,0,-1)]+[0]

then we give a flag to determine which kind of distance is used in this iteration.

The code are below
'''
s="PAYPALISHIRING"
trueRes="PHASIYIRPLIGAN"
numRows=5

if numRows>len(s):
    print(s==trueRes)
up=[0]+[ 2*i-1 for i in range(1,numRows+1)]
down=[2*i-1 for i in range(numRows-1,0,-1)]+[0]
       
newStr=""
        
for i in range(numRows):
    flag=True
    j=i
    newStr+=s[j]
    while True:
        if up[i]==0:
            j+=down[i]+1
        elif down[i]==0:
            j+=up[i]+1
        else:
            if flag:
                j+=down[i]+1
                flag=False
            else:
                j+=up[i]+1
                flag=True
        if j<=len(s)-1:
            newStr+=s[j]
        else:
            break
print(newStr==trueRes)


'''

'''