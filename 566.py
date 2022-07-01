import numpy as np

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        """try:
            matrix=np.array(mat).reshape(r,c)
            return matrix
        except ValueError:
            return mat
        """

        flatten = []
        new_mat = []
        for row in mat:
            for num in row:
                flatten.append(num)
        if r*c !=len(flatten):
            return mat
        else:
            for row in range(r):
                new_mat.append(flatten[row*c:row*c+c])
            return new_mat


s=Solution()
print(s.matrixReshape([[1,2],[3,4]],1,4))



"""import numpy as np

my_list = [[1,2],[3,4]]

matrix=np.array(my_list).reshape(1,4)

print(matrix)
"""
