class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp=[list(row) for row in zip(*matrix)]
        return tmp

s = Solution()
print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))