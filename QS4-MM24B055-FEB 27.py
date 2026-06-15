#qs 4 lambda function


# Lambda function to find square
square = lambda x: x ** 2

# Test
print(f"Square of 5: {square(5)}")        # 25


# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map() with lambda to find squares
squares = list(map(lambda x: x ** 2, numbers))

# Test

print(f"Original list: {numbers}")
print(f"Squares: {squares}")


# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() with lambda to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Test

print(f"Original list: {numbers}")
print(f"Even numbers: {even_numbers}")
