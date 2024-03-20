class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I']
        list = []
        for i in range(len(s)):
            list.append(s[i])
        i = 0
        j = len(s) - 1
        while (i < j):
            if list[i] not in vowels:
                i +=1
            elif list[j] not in vowels:
                j -= 1
            elif list[i] in vowels and list[j] in vowels:
                a = list[i]
                b = list[j]
                list[i] = b
                list[j] = a
                i += 1
                j -= 1
        return "".join(list)


if __name__ == "__main__":
    s =  Solution()
    result = s.reverseVowels(s = "leetcode")
    print(result)   