class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix)-1
        row = -1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <=  target <= matrix[m][-1]: #first element of the row is less than target
                row = m 
                break 
            elif matrix[m][0] > target: #first element of the row is greater than target
                r = m - 1
            else: 
                l = m + 1

        if row == -1: 
            return False 
        
        lp = 0 
        rp = len(matrix[0])-1
        while lp<=rp:
            m = (lp+rp)//2
            if target > matrix [row][m]:
                lp = m+1
            elif target < matrix [row][m]:
                rp = m -1
            else:
                return True 
        return False



        
