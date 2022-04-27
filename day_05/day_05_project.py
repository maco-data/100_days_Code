#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n") # 4 letter, 2 symbol, 2 number
nr_letters = int(input("How many letters would you like in your password?\n")) # ask for a number of letters

nr_symbols = int(input(f"How many symbols would you like?\n")) # ask for a number of symbols

nr_numbers = int(input(f"How many numbers would you like?\n")) # ask for a number of numbers


# empty list to save all the characters generated
password_list = [] 

# selects n random character from the letter list
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

# selects n random character from the symbols list
for sym in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# selects n random character from the numbers list
for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# randomly shuffles the password characters in the list
random.shuffle(password_list)

# add the list items as a concatanated string
rand_password = ""
for i in password_list:
    rand_password += i

# prints the final result
print(f"Here is your randomized password: {rand_password}\n")
