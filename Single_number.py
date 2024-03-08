'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
 
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] in new_list:
                new_list.remove(nums[i])
            else:
                new_list.append(nums[i])
        return new_list[0]

      



if __name__ == "__main__":
    s =  Solution()
    result = s.singleNumber([1])
    print(result)   