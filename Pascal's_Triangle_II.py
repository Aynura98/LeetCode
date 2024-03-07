'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        list = []
        first_row = [1]
        list.append(first_row)
        
        for i in range(1, rowIndex + 1) :
            prev_row = list[i - 1]
            current_row = [1]
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)
            list.append(current_row)
        return current_row
    
if __name__ == "__main__":
    s =  Solution()
    result = s.getRow(3)
    print(result)   