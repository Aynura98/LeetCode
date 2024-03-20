class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_list = []
        for i in range(len(magazine)):
            magazine_list.append(magazine[i])
        for j in range(len(ransomNote)):
            if ransomNote[j] not in magazine_list:
                return False
            else:    
                magazine_list.remove(ransomNote[j])
        return True
if __name__ == "__main__":
    s =  Solution()
    result = s.canConstruct(ransomNote = "aa", magazine = "ab")
    print(result)   