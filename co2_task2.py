correct_otp = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    otp = input("Enter OTP: ").strip()

    if otp == "":
        print("Blank entry. Try again.")
        continue

    if otp == correct_otp:
        print("OTP verified successfully!")
        break

    attempts += 1
    print("Wrong OTP!")

else:
    print("Account locked for 30 minutes.")

# Demonstration of pass
if False:
    pass
