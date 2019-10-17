'''
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

'''
My way:

Using a list to contain the index of minimal value, due to the constant time complexity of getMin().
The only problem is when the stack is empty, it will lead to the out of index. So we should add a dummy element at the buttom of the stack

The code are below
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s=[float("inf")]
        self.minIndex=[0]

    def push(self, x: int) -> None:
        self.s.append(x)
        if self.s[self.minIndex[-1]]>x:
            self.minIndex.append(len(self.s)-1)

    def pop(self) -> None:
        if self.minIndex[-1]==len(self.s)-1:
            self.minIndex.pop()
        self.s=self.s[:-1]

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s[self.minIndex[-1]]

    "Try any example yourself"