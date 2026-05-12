# MASTER PYTHON PROGRAM
# Covers:
# Variables
# Input
# Conditions
# for loop
# while loop
# break
# continue

# ---------------- VARIABLES ----------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = int(input("Enter a number: "))

print("\n----- USER DETAILS -----")
print("Name:", name)
print("Age:", age)
print("Favorite Number:", number)

# ---------------- CONDITIONS ----------------
print("\n----- CONDITIONS -----")

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Even or Odd
if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

# Positive / Negative / Zero
if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# ---------------- FOR LOOP ----------------
print("\n----- FOR LOOP -----")
print("Printing numbers from 1 to 5:")

for i in range(1, 6):
    print(i)

# Multiplication Table
print("\n----- MULTIPLICATION TABLE -----")

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# ---------------- WHILE LOOP ----------------
print("\n----- WHILE LOOP -----")

count = 1

while count <= 5:
    print("Count =", count)
    count += 1

# ---------------- BREAK EXAMPLE ----------------
print("\n----- BREAK EXAMPLE -----")

for i in range(10):
    if i == 5:
        print("Loop stopped at", i)
        break
    print(i)

# ---------------- CONTINUE EXAMPLE ----------------
print("\n----- CONTINUE EXAMPLE -----")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# ---------------- STRING LOOP ----------------
print("\n----- LOOP THROUGH STRING -----")

for ch in name:
    print(ch)

# ---------------- FINAL MESSAGE ----------------
print("\nProgram Finished Successfully!")