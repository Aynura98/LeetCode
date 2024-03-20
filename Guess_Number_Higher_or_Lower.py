# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):
def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        min = 0
        max = n
        guessed_number  = (min + max)/2
        while guess(guessed_number) !=0:
            if guess(guessed_number) == -1:
                max = guessed_number
            elif guess(guessed_number) == 1:
                min = guessed_number
                if min + 1 == n:
                    return n
            guessed_number  = ((min + max)/2)
        return (guessed_number)

if __name__ == "__main__":
    s =  Solution()
    result = s.guessNumber(n = 10)
    print(result)   