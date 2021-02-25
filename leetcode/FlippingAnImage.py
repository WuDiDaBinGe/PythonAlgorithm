class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        for i in range(len(A)):
            r_row=A[i][::-1]
            r_row_b=[1 if x==0 else 0 for x in r_row]
            result.append(r_row_b)
        return result

sol=Solution()
print(str(sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])))
