from functools import lru_cache
import sys

calls = 0


# Normal recursion
def ways_naive(n):

    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Recursion with memoisation
@lru_cache(maxsize=None)
def ways_memo(n):

    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# Iterative method
def ways_loop(n):

    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):

        c = a + b
        a = b
        b = c

    return b


# Check answers from 1 to 6
print("Number of ways:")

for n in range(1, 7):
    print(n, "steps:", ways_loop(n))


# Compare function calls for n = 10, 20, 25 and 30
print("\nFunction Call Comparison:")

for n in [10, 20, 25, 30]:

    calls = 0
    naive_result = ways_naive(n)
    naive_calls = calls

    calls = 0
    ways_memo.cache_clear()

    memo_result = ways_memo(n)
    memo_calls = calls

    print("\nn =", n)
    print("Naive result:", naive_result)
    print("Naive calls:", naive_calls)
    print("Memoised result:", memo_result)
    print("Memoised calls:", memo_calls)


# Test large staircase using iteration
print("\nWays for 1000 steps:", ways_loop(1000))

print("Recursion limit:", sys.getrecursionlimit())


# Test memoised recursion at 1000 steps
try:
    ways_memo.cache_clear()
    print("Memoised result for 1000:", ways_memo(1000))

except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded.")
