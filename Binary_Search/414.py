"""414 · Divide Two Integers"""
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        is_negative = False

        if dividend * divisor < 0:
            is_negative = True

        if dividend == 0:
            return 0

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0
        cnt = 0
        while dividend >= divisor:
            temp = divisor
            cnt = 1
            while dividend >= temp:
                ans += cnt
                dividend -= temp
                cnt <<= 1
                temp <<= 1

        if is_negative:
            ans = -ans

        if ans >= 1 << 31:
            ans = (1 << 31) - 1

        return ans
