print("Welcome to the tip calculator.")

get_bill = float(input("What was the total bill?: $"))

get_percentage = int(input("What percentage tip would you like to give?: %"))

get_headcount = int(input("How many people to split the bill?: "))

percentange = get_percentage / 100

total_tip = get_bill * percentange

total_bill = get_bill + total_tip

isSplit = total_bill / get_headcount

weighted_bill = round(total_bill)

rounded = round(total_bill, 2)

round_isSplit = round(isSplit)

round_isSplit = "{:.2f}".format(isSplit)

print(f"The total would be ${weighted_bill}, inclusion of the tip (%{percentange}). Since, it is a split bill. Each person should pay ${round_isSplit} each for {get_headcount} person(s).")

print("Thank you for using the tip calculator.")