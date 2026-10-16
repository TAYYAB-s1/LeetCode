class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        answer = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while temp + temp <= dividend:
                temp += temp
                multiple += multiple

            dividend -= temp
            answer += multiple

        if negative:
            answer = -answer

        return max(INT_MIN, min(INT_MAX, answer))