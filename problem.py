import math
"""
class Solution(object):
    def findGCD(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        
        print("The largest number in nums is",max(nums))
        print("The smallest number is",min(nums))

        def computeGCD(a,b):
            while b:
                a,b=b,a%b
            return a
        return computeGCD(max(nums),min(nums))

        

s=Solution()
print(s.findGCD([2,5,7,10]))

"""


"""class Solution(object):
    def isPalindrome(self, x):
        
        '''
        :type x: int
        :rtype: bool
        '''
        new_num=x
        rev_num=0
        if x<0:
            return False

        while x>0:
            remainder=x%10
            rev_num=rev_num*10+remainder
            x=x//10
        if new_num==rev_num:
            return True
        else:
            return False

s=Solution()
print(s.isPalindrome(-121))
"""
"""

class Solution(object):
    def secondHighest(self, s):
       '''
        :type s: str
        :rtype: int
        '''
        data=[]

        for i in s:
            if i.isdigit():
                if i not in data:
                    data.append(i)
        new_data=data
        if len(new_data)>1:
            new_data.remove(max(new_data))
            return max(new_data)
        else:
            return -1
        
        #for j in data:
            #if data[j]==max(data):

        
        
s=Solution()
print(s.secondHighest('dfa12321afd4'))

"""
"""
class Solution(object):
    def thirdMax(self, nums):
        
        print(nums)
        new=nums.remove(max(nums))
        print(new)
s=Solution()
print(s.thirdMax([3,2,1]))

"""
class Solution:
    def numIdenticalPairs(self, nums):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count+=1
        return count

s=Solution()
print(s.numIdenticalPairs([1,2,3]))