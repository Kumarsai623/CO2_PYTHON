import time


# Original recursive solution
def original_ways(n):

    if n <= 1:
        return 1

    return original_ways(n - 1) + original_ways(n - 2)


# Redesigned iterative solution
def redesigned_ways(n):

    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):

        c = a + b
        a = b
        b = c

    return b


# Test input
n = 30


# Measure original method
start = time.perf_counter()

original_result = original_ways(n)

original_time = time.perf_counter() - start


# Measure redesigned method
start = time.perf_counter()

redesigned_result = redesigned_ways(n)

redesigned_time = time.perf_counter() - start


# Display comparison
print("Input steps:", n)

print("\nOriginal Recursive Method")
print("Result:", original_result)
print("Execution time:", original_time)


print("\nRedesigned Iterative Method")
print("Result:", redesigned_result)
print("Execution time:", redesigned_time)


# Validate both results
if original_result == redesigned_result:
    print("\nValidation: SUCCESS")

else:
    print("\nValidation: FAILED")
