class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        if sum > 9 * num:
            return ""

        blank_good = [0] * num
        hold = sum
        for i in range(num):
            high = 9
            while high > 0 :
                if hold - high >= 0:
                    blank_good[i] = high
                    hold -= high
                    high -= 1           
                    break
                else:
                    high -= 1

            if hold <= 0: break    

        return "".join(str(d) for d in blank_good)


        
        