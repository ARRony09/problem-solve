class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=self.binary(nums,target)
        return self.expand(nums,index)


    def binary(self,nums,target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1
    
    def expand(self,nums,index):
        if index == -1:
            return [-1,-1]
        l=r=index
        
        while l>0 and nums[l-1]==nums[l]:
            l-=1

        while r<len(nums)-1 and nums[r+1]==nums[r]:
            r+=1
        return [l,r]




s=Solution()
print(s.searchRange([2,2],2))