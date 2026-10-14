class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        if sum > 9 * num:
            return ""

        blank_good = ''
        hold = sum
        for i in range(num):
            high = 9
            while high >= 0 and hold > 0:
                if hold - high >= 0:
                    blank_good += str(high)
                    hold -= high  
                    break
                else:
                    high -= 1

            if hold <= 0: blank_good += '0' * (num - len(blank_good))

        return blank_good


        
        