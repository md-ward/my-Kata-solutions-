

class Solution:
    def sum_squared_digits(self, n: int) -> int:
        sum_dig = 0
        while n:
            digit = n % 10
            sum_dig += digit ** 2
            n = n // 10
        return sum_dig

    def isHappy(self, n: int) -> bool:

        temp = set()
        while True:
            if n == 1:
                return True
            if n in temp:
                return False
            else:
                temp.add(n)
                n = self.sum_squared_digits(n)


print(Solution.isHappy(self=1, n=19))
