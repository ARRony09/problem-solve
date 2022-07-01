class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        return sum(list(set(nums)))*2 -sum(nums)
"""     
        res=0
        for i in nums:
            res^=i
        return res
        

s=Solution()
print(s.singleNumber([4,1,2,1,2]))