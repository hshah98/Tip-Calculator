print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? "))
split = int(input("How many people to split the bill? "))

amount_to_pay = total_bill / split * (1 + tip / 100)
print(f"Each person should pay: ${amount_to_pay:.2f}")
