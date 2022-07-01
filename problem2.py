"""class Solution(object):
    def thirdMax(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        data=[]
        for i in nums:
            if i not in data:
                data.append(i)

        if len(data)>2:
            data.sort()
            return data[-3]
        else:
            return max(nums)

    
s=Solution()
print(s.thirdMax([-1,3,2]))"""

"""
class Solution(object):
    def searchInsert(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: int
        '''
        for index,value in enumerate(nums):
           if value==target:
               return index
            else:



s=Solution()
print(s.searchInsert([1,3,5,6],5))"""

"""
from operator import index


class Solution(object):
    def maxProfit(self, prices):
        
        a=min(prices)
        inx=prices.index(a)
        data=[]
        for i in range(inx,len(prices)):
            #b=max(prices[i])
            data.append(prices[i])
            #print(b)
        b=max(data)
        profit=b-a
        return profit


s=Solution()
print(s.maxProfit([3,4,1,6]))"""

"""
class Solution(object):
    def maxProfit(self, prices):
        left=0
        right=1
        max_profit=0
        while right<len(prices):
            profit=prices[right]-prices[left]
            if prices[right]>prices[left]:
                max_profit=max(profit,max_profit)
            else:
                left=right
            right += 1
        return max_profit


s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))"""



"""
class Solution(object):
    def maxProfit(self, prices):
        left=0
        right=1
        max_profit=0
        total_profit=0
        while right<len(prices):
            if max_profit>=1:
                left=right+1
                right=right+2
            profit=prices[right]-prices[left]
            if prices[right]>prices[left]:
                max_profit=max(profit,max_profit)
            else:
                left=right
            right += 1
        return max_profit


s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))"""