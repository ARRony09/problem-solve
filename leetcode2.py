class Solution:
    def mySqrt(self, x):
        low=0
        high=x
        while(low<=high):
            mid=low+(high-low)//2

            if mid*mid>x:
                high=mid-1
            else:
                low=mid+1
        return high
        
s=Solution()
print(s.mySqrt(8))