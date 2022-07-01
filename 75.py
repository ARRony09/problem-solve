class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """list=[]
        list1=[]
        list2=[]
        list3=[]
        for i in nums:
            if i==0:
                list1.append(i)
            elif i==1:
                list2.append(i)
            else:
                list3.append(i)
        
        list1.extend(list2)
        list1.extend(list3)
        nums=list1
        print(nums)"""

        """for i in nums:
            if i==2:
                nums.remove(i)   
                nums.append(i)
            elif i==0:
                nums=[i]+nums
            elif i==1:
                if nums[0]==0:
                    nums=nums[1]+i
        print(nums)"""
        
s=Solution()
s.sortColors([2,0,2,1,1,0])