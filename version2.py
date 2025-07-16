import random, string

# improved version, realised that the one I took inspiration from longed stuff out.
# changes: one list for all chars, uses choice instead of shuffling/partitioning
#          uses a list comprehension to generate the password instead of 2 for loops.

chars = string.ascii_letters + string.digits + string.punctuation

print(("It's required you use a password length of at least 8 characters."
       "However, it's recommended to use 12-16 characters for a stronger password\n"
       "There's no maximum, just ensure you can safely store it and remember it!\n"))

while True:
    try:
        length_input = int(input("What length do you want the password to be? "))
        if length_input < 8:
            print("The password must be of length at least 8.")
        else:
            break

    except ValueError:
        print("You must enter an integer greater than 8.")

result = [random.choice(chars) for i in range(length_input)]
random.shuffle(result)
password = ''.join(result)

print(f"Your new password is: {password}")

