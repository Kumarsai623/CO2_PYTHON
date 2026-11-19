units = int(input("Enter electricity units: "))
ration_card = input("Do you have a ration card? (yes/no): ").lower()
senior = input("Is any member above 80 years? (yes/no): ").lower()

# Method 1: Separate if statements
print("\nUsing Separate If Statements:")

if units <= 100:
    print("Full Subsidy")

if 101 <= units <= 200 and ration_card == "yes":
    print("Partial Subsidy")

if units > 200 and senior == "yes":
    print("Special Subsidy")

if not (units <= 100 or
        (101 <= units <= 200 and ration_card == "yes") or
        (units > 200 and senior == "yes")):
    print("No Subsidy")

# Method 2: if-elif-else
print("\nUsing If-Elif-Else:")

if units <= 100:
    result = "Full Subsidy"
elif 101 <= units <= 200 and ration_card == "yes":
    result = "Partial Subsidy"
elif units > 200 and senior == "yes":
    result = "Special Subsidy"
else:
    result = "No Subsidy"

print("Final Decision:", result)
