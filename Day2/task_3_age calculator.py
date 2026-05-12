# AGE CALCULATOR PROGRAM

from datetime import date

print("===== AGE CALCULATOR =====")

# Taking birth year input
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Current date
today = date.today()

# Calculating age
age = today.year - birth_year

# Checking if birthday has occurred this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Output
print("\n----- RESULT -----")
print("Current Date :", today)
print("Your Age is :", age, "years")

# Extra Information
print("\nYou were born on:")
print(birth_day, "/", birth_month, "/", birth_year)

print("\nProgram Finished Successfully!")