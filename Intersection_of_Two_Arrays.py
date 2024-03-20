class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                if nums1[i] not in new_list:
                    new_list.append(nums1[i])
        return new_list

if __name__ == "__main__":
    s =  Solution()
    result = s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
    print(result)   