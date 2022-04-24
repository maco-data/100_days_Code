# Ask for the city name
def city_name():
    city = input("What is the name of the city you grew up?\n")
    return city


# Ask for a pet name
def pet_name():
    pet = input("What is the name of your pet?\n")
    return pet


# Welcomes user, ask execute question and generates band name
def greeting():
    print("Welcome to Band Name Generator")
    c_name = city_name()
    p_name = pet_name()
    print(f"They name of your band is {c_name} {p_name}!")

greeting()