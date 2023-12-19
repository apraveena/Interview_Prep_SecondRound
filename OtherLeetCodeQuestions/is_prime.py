
def is_prime(n: int) -> int:
    if n == 1: return False
    for i in range(2, 1 + n//2):
        if n % i == 0 and n != i:
            return False
    return True

def count_primes(n):
    count = 0
    for i in range(1, n):
        if is_prime(i):
            count += 1
    return count

print(count_primes(10))