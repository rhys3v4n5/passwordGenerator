import random, string

# written by rhys for personal use, took inspo from geeks for geeks, modified myself
# just a disclaimer ig
print("We require you use a password length of at least 8. However, it is recommended to use 12-16 characters")

# lower case and uppercase chars, can split this
lowercase_chars, uppercase_chars = list(string.ascii_lowercase), list(string.ascii_uppercase)
number_chars = list(string.digits)
special_chars = list(string.punctuation)

while True:
    try:
        length_input = int(input("What length do you want the password? "))
        if length_input < 8:
            print("The password must be of length at least 8.")
        else:
            break

    except ValueError:
        print("You must enter an integer greater than 8.")

# shuffle the order randomly so we always get diff sequenes
random.shuffle(lowercase_chars)
random.shuffle(uppercase_chars)
random.shuffle(number_chars)
random.shuffle(special_chars)

partition1 = round(length_input * (30/100))
partition2 = round(length_input * (20/100))

result = []

for i in range(partition1):
    result.append(random.choice(lowercase_chars))
    result.append(random.choice(uppercase_chars))

for i in range(partition2):
    result.append(random.choice(number_chars))
    result.append(random.choice(special_chars))

random.shuffle(result)

password = "".join(result)
print(f"The generated password is: {password}")



