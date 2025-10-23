age = int(input("Enter your age: "))

if age < 0:
    print("Age can't be negative")
elif age <= 18:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")
