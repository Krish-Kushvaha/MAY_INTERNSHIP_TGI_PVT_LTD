# Basic Python Program
# This program covers:
# - Variables
# - Input/Output
# - Data Types
# - Operators
# - Conditions
# - Loops
# - Functions
# - Lists
# - Dictionaries

# Function
def greet(name):
    return f"Hello, {name}!"

# Taking input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Variables and Data Types
is_student = True
height = 5.8

# Printing values
print("\n--- User Information ---")
print("Name:", name)
print("Age:", age)
print("Student:", is_student)
print("Height:", height)

# Function call
message = greet(name)
print(message)

# Conditions
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# List
subjects = ["Python", "AI", "ML"]

print("\n--- Subjects List ---")
for subject in subjects:
    print(subject)

# Dictionary
marks = {
    "Python": 90,
    "AI": 85,
    "ML": 88
}

print("\n--- Marks ---")
for key, value in marks.items():
    print(key, ":", value)

# Loop
print("\n--- Numbers from 1 to 5 ---")
for i in range(1, 6):
    print(i)

# While Loop
count = 1
print("\n--- While Loop ---")
while count <= 3:
    print("Count =", count)
    count += 1

# Operators
a = 10
b = 5

print("\n--- Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Final message
print("\nProgram Finished Successfully!")