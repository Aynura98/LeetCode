class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in new_list:
                new_list.append(nums[i])
        if len(new_list) < 3:
            return new_list[-1]
        else:
            return new_list[-3]
if __name__ == "__main__":
    s =  Solution()
    result = s.thirdMax(nums = [2,2,3,1])
    print(result)   