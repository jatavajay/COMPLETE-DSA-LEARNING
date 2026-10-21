class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        res = []
        top,bottom = 0, m-1
        left,right = 0,n-1

        while top <= bottom and left <= right:
            # Left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            # Top to bottom
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1
            # Right to left
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1
            # Bottom to top
            if left <= right:
                for l in range(bottom, top - 1, -1):
                    res.append(matrix[l][left])
                left += 1
        return res