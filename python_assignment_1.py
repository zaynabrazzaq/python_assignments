# 1. Create a list of numbers
my_numbers =[3,4,5,6]
factorials = []

# 2. Define a custom function to calculate a factorial
def calculate_factorial(n):
    factorial_total = 1
    # Loop from 1 up to the number (n) and multiply
    for i in range(1, n + 1):
        factorial_total *= i
    return factorial_total

# 3. Loop through the list and use our custom function
for num in my_numbers:
    result = calculate_factorial(num)
    factorials.append(result)

# 4. Print the results
print("Original list of numbers:", my_numbers)
print("Factorials of those numbers:", factorials)