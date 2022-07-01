from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate=None
        count=0
        for n in nums:
            if candidate == None:
                candidate=n
                count+=1
            elif candidate==n:
                count+=1
            elif n!=candidate and candidate==1:
                candidate=None
                count-=1
            elif n!= candidate:
                count-=1
        return candidate
s=Solution()
print(s.majorityElement([3,2,3]))