def sum_even_numbers(n):
    result = 0
    i = 2
    while i <= n:
        result += i
        i += 2
    return result

n = int(input("Enter a positive integer 'n': "))

if n < 1:
    print("Please enter a positive integer.")
else:
    even_sum = sum_even_numbers(n)
    print(f"The sum of even numbers from 1 to {n} is: {even_sum}")
