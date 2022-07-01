#stack
from collections import deque

"""
stack=deque()

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print(stack)

print("Element popped")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())"""
"""

from collections import deque


class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def reverse_string(self,val):
        return val[::-1]

def is_match(ch1,ch2):
        match_dict={
            ')':'(',
            '}':'{',
            ']':'['
        }

        return match_dict[ch1] == ch2

def is_balanaced(val):
        stack=[]
        for ch in val:
            if ch=='(' or  ch=='{' or  ch=='[':
                stack.push(ch)
            if ch==')' or  ch=='}' or  ch==']':
                if len(stack)==0:
                    return False
                if not is_match(ch,stack.pop()):
                    return False



s=Stack()
print(s.reverse_string("We will conquere COVID-19"))
print(s.is_balanced("((a+b))"))
"""
