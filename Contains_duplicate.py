class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_set = set()
        
        for i in nums:
            if i in new_set:
                return True
            else:
                new_set.add(i)
        return False


if __name__ == "__main__":
    s =  Solution()
    result = s.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])
    print(result)   
