# import modules
import secrets
import string
from datetime import datetime


# joining all the conditions and requirements to make a number of passwords requested
# using secrets module to generates cryptographically strong random numbers passwords
def generate(length, character_set):
    password = ''.join(secrets.choice(character_set) for _ in range(length))
    return password


# user input on how long the password is required
def howLong():
    while True:
        try:
            length = int(input("Password length required: "))
            # added error incase password is not long enough or invalid input
            if length < 1:
                print("Password should be longer then 1")
            else:
                return length
        except ValueError:
            print("Invalid input.")


# included special characters into password if needed, y or n
def symbols():
    while True:
        response = input("Special characters? (y/n): ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("Invalid input.")


# user input including digits, y or n
def get_include_digits():
    while True:
        response = input("Include digits? (y/n): ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("Invalid input.")


# this function will be adding ascii letters, digits and special characters to set
def requirements(specialC, include_digits):
    character_set = string.ascii_letters
    if include_digits:
        character_set += string.digits
    if specialC:
        character_set += string.punctuation
    return character_set


# creating a score and the more complex the password is has more points
def rating(password):
    score = 0
    # Check password length, more points for longer passwords
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 2
    if len(password) >= 16:
        score += 3
    # adding extra points for special charactors, digits, lower and upper
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    return score

# how many passwords to be generated
def howMany(num_passwords, length, specialC, include_digits):
    passwords = []
    for _ in range(num_passwords):
        password = generate(length, requirements(specialC, include_digits))
        passwords.append(password)
    return passwords

# main function including banner and time then into running the functions above
def main():
    print("-" * 55)
    print("Password Generator")
    print("Time: " + str(datetime.now()))
    print("-" * 55)
    # how long is the password going to be
    length = howLong()
    # special characters included or not
    specialC = symbols()
    # if digits needed to be added to the password
    include_digits = get_include_digits()
    # asking for amount of passwords to generate
    num_passwords = int(input("Number of passwords to generate: "))
    # putting all the variables together to create a list of passwords
    passwords = howMany(num_passwords, length, specialC, include_digits)
    print("-" * 55)
    print("\nRandom Generated Passwords:")

    # print all the passwords in the list
    for password in passwords:
        print(password)
        strength = rating(password)
        print("Password Strength:", strength, "out of 10")

if __name__ == "__main__":
    main()
