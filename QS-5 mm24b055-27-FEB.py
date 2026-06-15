# Recursion

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test
print("FACTORIAL:")
print(f"5! = {factorial(5)}")      # 120
print(f"0! = {factorial(0)}")      # 1
print(f"7! = {factorial(7)}")      # 5040

def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")

print(f"\nfib(10) = {fibonacci(10)}")

#c part
def sum_of_digits(n):
    # Handle negative numbers by taking absolute value
    n = abs(n)
    
    # Base case: if number is 0, sum is 0
    if n == 0:
        return 0
    # Recursive case: last digit + sum of remaining digits
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Test
print(f"Sum of digits of 12345: {sum_of_digits(12345)}")      # 15
print(f"Sum of digits of 7: {sum_of_digits(7)}")              # 7




# # More efficient version with memoization (to avoid repeated calculations)
# def fibonacci_memo(n, memo={}):
#     # Check if already calculated
#     if n in memo:
#         return memo[n]
    
#     # Base cases
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     # Calculate and store in memo
#     memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
#     return memo[n]
# print(f"fib(10) with memo = {fibonacci_memo(10)}")  # 55