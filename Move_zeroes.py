class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                length -= 1
            else:
                i += 1
                    
        

if __name__ == "__main__":
    s =  Solution()
    result = s.moveZeroes(nums = [0,0,1])
    print(result)   
