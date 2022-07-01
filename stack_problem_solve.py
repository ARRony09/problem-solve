"""from collections import deque
from queue import LifoQueue



class MinStack(object):

    def __init__(self):
        self.container=LifoQueue()

    def push(self, val):
        self.container.put(val)
        

    def pop(self):
        
        return self.container.get()
        

    def top(self):
        return self.container.get_nowait()
        

    def getMin(self):
        return min(self.container)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

s=MinStack()
s.push(5)
s.push(10)
s.push(3)
s.push(20)
s.push(1)
print(s.pop())
print(s.top())
print(s.getMin())
"""



"""
def is_match(ch1, ch2):
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        return match_dict[ch1] == ch2

class Solution(object):
    def isValid(self, s):
        stack=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch == '[':
                stack.append(ch)
            if ch==')' or ch=='}' or ch == ']':
                if len(stack)==0:
                    return False
                if not is_match(ch,stack.pop()):
                    return False

        return len(stack)==0

s=Solution()
print(s.isValid('(}'))"""

"""
class Solution(object):
    def maxDepth(self, s):
        stack=[]
        depth=0
        max_depth=0

        for ch in s:
            if ch=="(":
                stack.append(ch)
                depth+=1
                max_depth=max(max_depth,depth)
            if ch==")":
                stack.pop()
                depth-=1
        if len(stack)==0:
            return max_depth
            


s=Solution()
print(s.maxDepth("(1)+((2))+(((3)))"))"""




"""

class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if i in stack:
                stack.pop()
            else:
                stack.append(i)
            
        new_stack=""
        a=new_stack.join(stack)
        return a
        
s=Solution()
print(s.removeDuplicates("aababaab"))"""
"""
class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
            
        new_stack=""
        a=new_stack.join(stack)
        return a

s=Solution()
print(s.removeDuplicates("aababaab"))
"""


class Solution(object):
    def removeDuplicates(self, s,k):
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
            
        new_stack=""
        a=new_stack.join(stack)
        return a

s=Solution()
print(s.removeDuplicates("deeedbbcccbdaa"))
