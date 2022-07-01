class Solution(object):
    def containsDuplicate(self, nums):
        list=[]
        for i in nums:
            if i not in list:
                list.append(i)
        if len(list)==len(nums):
            return False
        else:
            return True

s=Solution()
print(s.containsDuplicate([2,14,18,22,22]))
