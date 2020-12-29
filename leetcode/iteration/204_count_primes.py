import time


def countPrimes(n: int) -> int:
    start_time = time.time()
    prime_numbers = 0
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers += 1
    end_time = time.time()
    print(f"total time: {(end_time - start_time) % 60}")
    return prime_numbers


# 1. Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).

# 2. Initially, let p equal 2, the first prime number.

# 3. Starting from p2, count up in increments of p and mark each of these
# numbers greater than or equal to p2 itself in the list.
# These numbers will be p(p+1), p(p+2), p(p+3), etc..

# 4. Find the first number greater than p in the list that is not marked.
# If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime),
# and repeat from step 3.

def sieve_of_eratosthenes(n):
    start_time = time.time()
    nums = [True] * n

    i = 2
    while i * i < n:
        if nums[i]:
            j = 2
            while j * i < n:
                nums[j * i] = False
                j += 1

        i += 1

    prime_count = 0
    for n in nums[2:]:
        if n:
            prime_count += 1

    end_time = time.time()
    print(f"total time: {(end_time - start_time) % 60}")
    return prime_count


print(countPrimes(20000))
print(sieve_of_eratosthenes(20000))
