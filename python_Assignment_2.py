# Q1: Student Marks
stdmarks = []

# 1. Enable users to enter names and marks
print("--- Enter Student Data (Type 'stop' as the name to finish) ---")
while True:
    name = input("Enter student name: ")
    if name.lower() == 'stop':
        break
    mark = float(input(f"Enter mark for {name}: "))
    # Storing as [name, mark]
    stdmarks.append([name, mark])

# 2. Insert a new name and mark to the location "3"
if len(stdmarks) >= 3:
    stdmarks.insert(3, ["InsertedName", 90.0])
else:
    # Handle lists smaller than 3 items
    stdmarks.append(["InsertedName", 90.0])

# 3. Replace the third name with a new name (index 2)
if len(stdmarks) >= 3:
    stdmarks[2][0] = "ReplacedName"

# 4. Find all students who passed
passedStudents = []
for student in stdmarks:
    # Check if mark is >= 50
    if student[1] >= 50:
        passedStudents.append(student)

# 5. Display all passed students
print("\n--- Passed Students ---")
for student in passedStudents:
    print(f"Name: {student[0]} | Mark: {student[1]}")


# Q2: Sum of digits using a while loop
num = int(input("Enter a positive integer: "))
total_sum = 0
temp = num

while temp > 0:
    digit = temp % 10  # Extract last digit
    total_sum += digit
    temp //= 10  # Remove last digit

print(f"The sum of the digits of {num} is {total_sum}.")


# Q3: Factorial of a number
n = int(input("Enter a number to find its factorial: "))
factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")


# Q4: Largest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Assume first number is largest initially
largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(f"The largest number is {largest}.")


# Q5: Sum of numbers from 1 to N
n = int(input("Enter a positive integer N: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"The sum of numbers from 1 to {n} is {total}.")


# Q6: Count the number of digits
num = int(input("Enter an integer: "))

# Use absolute value for negative numbers, convert to string to count length
digit_count = len(str(abs(num)))

print(f"The number of digits in your integer is: {digit_count}")


# Q7: Prime numbers stored in a tuple
primes_list = []

print("--- Enter numbers (Type 'stop' to finish) ---")
while True:
    user_input = input("Enter an integer: ")
    if user_input.lower() == 'stop':
        break

    num = int(user_input)
    is_prime = True

    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(num)

# Convert list to tuple
primes_tuple = tuple(primes_list)

print("\nTuple of prime numbers:", primes_tuple)


# Q8: Sort employee names
employees = []

print("--- Enter Employee Names (Type 'stop' to finish) ---")
while True:
    name = input("Enter employee name: ")
    if name.lower() == 'stop':
        break
    employees.append(name)

employees.sort()

print("\n--- Alphabetical List of Employees ---")
for emp in employees:
    print(emp)