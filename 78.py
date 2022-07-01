class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flatten=[]
        for row in matrix:
            for num in row:
                flatten.append(num)
        if target in flatten:
            return True
        else:
            return False

s=Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
