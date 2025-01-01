class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()
        while n != 1 and n not in temp:
            temp.add(n)
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum 
        return n == 1
