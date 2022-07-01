class Solution:
    def maxSubArray(self, nums):
        """i=0
        j=1
        c=[nums[0]]
        for j in range(1,len(nums)):
            if c[i]+nums[j]> nums[j]:
                t=c[i]+nums[j]
            else:
                t=nums[j]
            c.append(t)
            i+=1
            j+=1
        return max(c)"""
        if len(nums)<2:
            return nums[0]
        prev_sum=0

        max_sum=nums[0]
        for i in nums:
            prev_sum+=i
            if prev_sum>max_sum:
                max_sum=prev_sum
            if prev_sum<0:
                prev_sum=0
        return max_sum

s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
