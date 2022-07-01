from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):

        result = []
        c = Counter(nums1)
        print(c)
        for i in nums2:
            if c[i]>1:
                result.append(i)
                c[i]-=1
        return result
        """
        [1,2,2,1],[2,2]
        [4,9,5],[9,4,9,8,4]
        """


s=Solution()
print(s.intersect([4,9,5],[9,4,9,8,4]))
