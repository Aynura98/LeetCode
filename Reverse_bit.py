class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reversed_num = 0
        
        # Iterate over all 32 bits of the given number
        for i in range(32):
            # Left shift the reversed number by 1 and add the last bit of the given number to it
            reversed_num = (reversed_num << 1) | (n & 1)
            # To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1
            n >>= 1
        
        # Return the reversed number
        return reversed_num
    
if __name__ == "__main__":
    s =  Solution()
    abc = s.reverseBits(11111111111111111111111111111101)
    print(abc)  