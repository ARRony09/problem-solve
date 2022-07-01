"""class Solution(object):
    def findGCD(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        a=max(nums)
        b=min(nums)
        
        print("The largest number in nums is",a)
        print("The smallest number is",b)
        
        def computeGCD(a,b):
            if b==0:
                return a
            else:
                return computeGCD(b,a%b)
        return b


s=Solution()
print(s.findGCD([3,3]))"""
"""
expanse=[2200,2350,2600,2130,2190,2000]
            
#sol 1
extra_expanse=expanse[1]-expanse[0]
print(extra_expanse)
                    
total_expanse= expanse[0]+expanse[1]+expanse[2]
print(total_expanse)

expanse.append(1980)
print(expanse)

for i in expanse:
    if i == 2000:
        print(i)

expanse[3]=expanse[3]-200
print(expanse)"""

"""
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove(heros[5])
print(heros)
heros.insert(3,'black panther')
print(heros)

heros=list(map(lambda x:x.replace('thor',"Doctor strange"),heros))
print(heros)

heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)
"""

"""
inp=input("Enter your input ")
for i in range(0,int(inp)):
    if i%2!=0:
        print(i)
"""
"""
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))"""


class Solution(object):
    def longestCommonPrefix(self, strs):

        if len(strs)==0:
            return
        elif len(strs)==1:
            return "".join(strs)
        else:
            x=strs.pop(0)
            list=[]
            for i in x:
                list.append(i)
            #return list
            prefix=strs[0][1]
            list2=[]
            for i in list:
                for j in range(len(strs)):
                    if i in strs[0][1]:
                        list2.append(i)
            
            a="".join(str(i) for i in list2)
            return a


s=Solution()
print(s.longestCommonPrefix(["reflower","flow","flight"]))
