# convert the input into a float if the condition if met
def tip_percentage():
    tip_choice = input("What percentage tip would you like to give? 10, 12, or 15? ")
    if tip_choice == "10":
        return 1.1
    elif tip_choice == "12":
        return  1.12
    elif tip_choice == "15":
        return  1.15
    else:
        return (float(tip_choice) / 100) + 1
        

# Ask for inputs then calculated the total bill with the tip included
def tip_cal():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? $"))
    total_people = int(input("How many people to split the bill? "))
    tip_given = tip_percentage()
    bill_split = total_bill / total_people * tip_given
    print(f"Each person should pay: ${round(bill_split, 2)}")

tip_cal()