class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
if __name__ == "__main__":
    s =  Solution()
    result = s.missingNumber(nums = [0,1])
    print(result)   