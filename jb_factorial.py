def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#Test the factorial function
number = 34
print(f"Factorial of {number} is: {factorial(number)}")