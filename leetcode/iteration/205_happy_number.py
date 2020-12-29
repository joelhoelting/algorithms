def isHappy(self, n: int) -> bool:
    seen = set()

    while n != 1:
        sum = 0
        while n > 0:
            sum += (n % 10) * (n % 10)
            n //= 10
        n = sum

        if sum in seen:
            return False

        seen.add(n)

    return True
