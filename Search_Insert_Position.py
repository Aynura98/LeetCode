'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)

        if(target > nums[length - 1]):
            return length

        i = 0
        while i < length:
            if nums[i] == target or target < nums[i]:
                return i
            else:
                i += 1
            
            
             
if __name__ == "__main__":
    s =  Solution()
    result = s.searchInsert([1,3,5,6],7)
    print(result)            