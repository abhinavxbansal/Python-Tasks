# Program to calculate factorial of a number

def factorial(n):
    result = 1
    for i in range(1, n + 1):   # multiply numbers from 1 to n
        result *= i
    return result

# Call the function with a sample number
num = 5
print(f"The factorial of {num} is: {factorial(num)}")
