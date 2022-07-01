class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #nums1[:]=sorted(nums1[:m]+nums2[:n])
        del(nums1[m:])
        nums1.extend(nums2)
        nums1.sort()
        return nums1



        """for i in nums2:
            if i != 0:
                nums1.append(i)
        nums1=sorted(nums1)
        #print(a)
        if len(nums1)==m+n:
            return nums1
        else:
            b=m+n
            c=len(nums1)-b
            del nums1[0:c]
            return nums1"""


s=Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
