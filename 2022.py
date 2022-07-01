import numpy as np
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        [1,2,3,4],2,2
        """
        try:
            matrix=np.array(original).reshape(m,n)
            return matrix
        except ValueError:
            return []



s=Solution()
print(s.construct2DArray([1,2,3,4],2,2))
