def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

# Prompt the user to enter a value for 'n'
n = int(input("Enter a positive integer 'n': "))

# Check if 'n' is positive
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and display the factorial
    result = calculate_factorial(n)
    print(f"The factorial of {n} is: {result}")
