"""class Solution(object):
    def removeDuplicates(self, nums):

        
        
        count=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[count]:
                nums[count+1]=nums[i]
                count+=1
        return count+1


s=Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
"""

"""
class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
        

s=Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))"""
"""
class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


s=Solution()
print(s.strStr("aaaaa",'bba'))"""
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        return len(a[-1])

        
s=Solution()
print(s.lengthOfLastWord("luffy is still joyboy"))"""

"""
class Solution(object):
    def plusOne(self, digits):
        sum=digits[-1]+1
        a=str(sum)
        if len(a)>1:
            numList=[int(digit) for digit in a]
            return numList
            
        else:
            digits[-1]=digits[-1]+1
            return digits

s=Solution()
print(s.plusOne([9,9]))"""

"""
class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1

        while(i>=0):
            if (digits[i]==9):
                digits[i]=0
                i-=1
            else:
                digits[i]+=1
                return digits
        digits.insert(0,1)
        return digits

s=Solution()
print(s.plusOne([9]))"""
"""
import re

class Solution(object):
    def longestCommonPrefix(self, strs):
        longest_prefix=''
        for i in range(min([len(word) for word in strs])):
            add_letter=True
            letter_of_interest=strs[0][i]
            for w in strs[1:]:
                if w[i] != letter_of_interest:
                    add_letter=False
            if add_letter:
                longest_prefix+=letter_of_interest
            else:
                break
        return longest_prefix


s=Solution()
print(s.longestCommonPrefix(["reflower","flow","flight"]))

"""
"""import re
class Solution(object):
    def isPalindrome(self, s):
        a=re.sub(r'[^a-zA-Z0-9]','',s.lower())
        rev_str=a[::-1]
        if a==rev_str:
            return True
        else:
            return False
        
s=Solution()
print(s.isPalindrome(" "))"""

"""
class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return low
s=Solution()
print(s.searchInsert([1,3,5,6],7))"""

"""
class Solution(object):
    def targetIndices(self, nums, target):
        a=sorted(nums)
        low=0
        high=len(a)-1
        list=[]
        while low<=high:
            mid=(high+low)//2
            if len(a)>mid and a[mid]==target:
                list.append(mid)
                a.pop(mid)
                high=mid+1
            elif len(a)>mid and a[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return list[::-1]
        
s=Solution()
print(s.targetIndices([100,1,100],100))"""
"""
class Solution:
    def targetIndices(self,nums,target):
        nums.sort()
        
        def bin_search(arr, t, lower=True):
            left, right = 0, len(arr) -1 
            
            while left <= right:

                mid = (left + right) // 2

                if arr[mid] == t:
                    if lower:
                        if mid == left or nums[mid] != arr[mid - 1]:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        if mid == right or arr[mid] != arr[mid + 1]:
                            return mid
                        else:
                            left = mid + 1
                        
                elif arr[mid] > t:
                    right = mid - 1 
                elif nums[mid] < t:
                    left = mid + 1
            
            return -1
        
        start, end = bin_search(nums, target), bin_search(nums, target, False)
        
        if start < 0 and end < 0:
            return []
        
        return list(range(start, end + 1))

s=Solution()
print(s.targetIndices([100,1,100],100))"""
"""
class Solution(object):
    def findPeakElement(self, nums):
        
        '''a=max(nums)
        b=nums.index(a)
        return b
        '''
        low=0
        high=len(nums)-1

        while low<=high:
            mid=(low+high)//2

            if low==high:
                return mid
            if nums[mid]>nums[mid+1]:
                high = mid
            else:
                low=mid+1


s=Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))"""

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=0
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i]>nums[j] and nums[j]>nums[j+1]:
                    flag+=1



        
        


s=Solution()
print(s.countHillValley([6,6,5,5,4,1]))