import re


def check_strength(username, age, password):
    if (check_length(password) and check_characters(password)
            and check_special_words(username, age, password)):
        print("Strong password!")
    else:
        print("This password is too weak!")


def check_length(password):
    if len(password) < 8:
        return False

    return True


def check_characters(password):
    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True


# check for if the persons sensitive info is in the password
def check_special_words(password, name, dob):
    if name in password:
        return True
    elif dob in password:
        return True
    return False


entered_name = input("Please enter your username: ")
# where dob stands for date of birth (the year)
entered_dob = input("Please enter your birthyear: ")
entered_password = "#Mark2000"

check_strength(entered_name, entered_dob, entered_password)