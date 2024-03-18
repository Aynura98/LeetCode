class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        for i in range(len(nums)):
            if nums.count(nums[i]) > len(nums)/2:
                return nums[i]

if __name__ == "__main__":
    s =  Solution()
    result = s.majorityElement(nums = [2,2,1,1,1,2,2])
    print(result)   
