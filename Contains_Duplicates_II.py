class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        new_dic = {}
        
        for i in range(len(nums)):
            if nums[i] in new_dic and abs(i - new_dic[nums[i]]) <= k:
                return True 
            else:
                new_dic[nums[i]] = i
        return False

        

if __name__ == "__main__":
    s =  Solution()
    result = s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
    print(result)   
