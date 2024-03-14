class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        str_n = str(n)
        sum = 0
        list = []
        while sum != 1:
            for i in range(len(str_n)):
                sum += int(str_n[i])*int(str_n[i])
            if sum != 1 and (sum not in list):
                str_n = str(sum)
                list.append(sum)
                sum = 0
            elif sum in list:
                return False
        return True

if __name__ == "__main__":
    s =  Solution()
    result = s.isHappy(n = 2)
    print(result)   