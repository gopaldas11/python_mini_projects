full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    str_dots = "●" * strength + "○" * (10 - strength)
    int_dots = "●" * intelligence + "○" * (10 - intelligence)
    cha_dots = "●" * charisma + "○" * (10 - charisma)

    return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"


# Here we will take - NEW INPUT PROCESS
# 1. Taking the name input directly as a string
user_name = input("Enter character name: ")

try:
    # 2. Take the stats as inputs and instantly convert them to integers
    user_str = int(input("Enter Strength (1-4): "))
    user_int = int(input("Enter Intelligence (1-4): "))
    user_cha = int(input("Enter Charisma (1-4): "))

    # 3. Pass the collected variables into your original function
    result = create_character(user_name, user_str, user_int, user_cha)
    print("\n" + result)

except ValueError:
    # This will handle the case where a user types letters instead of a number for stats
    print("\nAll stats should be integers")
