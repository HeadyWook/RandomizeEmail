#!/usr/bin/env python3

"""This program creates random usernames and passwords for throw away email addresses. It generates two
random sets of strings. The length of which is determined by the user. The character set includes lower (i.e.,
abc...xyz) and uppercase (i.e., ABC...XYZ) letters and numbers (i.e., 0-9). The purpose of this program is to
automate online character randomizers on a local machine.

For example, Bob wants to create a throw away email address to sign up for some service. He can access
https://mail.cock.li through Tor, run this program on his local machine, generate a random username and password,
and copy and paste each string into the respective fields. Bob does not have to spend the mental effort to make up a
username and password. He can also avoid using variants of existing emails. He skip the online character randomizer.
Bob can then do what he likes with the string sets. He may delete them or save them in a .txt file for later,
like so:

randomThrowAwayEmail.txt
https://mail.cock.li
Email:JuGAgEGqNhW5qVK@cock.li
Username: JuGAgEGqNhW5qVK
Password: qT2TN0RLheImT2M
"""

# Import the random module.
import random
# Import the datetime module.
import datetime

# Get today's data and time and format it.
DATETIME = datetime.datetime.now().strftime("%c")

# A list of lowercase (i.e., abc...xyz) and uppercase (i.e., ABC...XYZ) letters and numbers (i.e., 0-9).
CHARACTER_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Empty lists for the username and password characters.
USERNAME = []
PASSWORD = []


# Display the introduction.
def display_intro():
    # Print a divider
    print("=" * 25)
    # Set the intro message and print it in all caps.
    intro_message = "Welcome to the email username and password randomizer."
    print(intro_message.upper())
    # Print today's date and time.
    print("Today is:", DATETIME)
    print("How many random characters would you like to generate?")
    # Print a divider
    print("=" * 25)


# Prompt the user to select the character length of username/password.
def get_length():
    while True:
        try:
            # Prompt the user for an integer input on the character length.
            length = int(input("Enter length: "))
            # Check for a length greater than zero.
            # If the length is less than or equal to zero, then print an error message and continue the prompt.
            if length <= 0:
                print("Pick a number greater than zero.\n")
                continue
            else:
                # If the length is valid, then end the while loop and return length.
                return length
        # Accept a value error, print an error message, and continue the prompt.
        except ValueError:
            print("Invalid entry. Try again.\n")
            continue


# Generate two random character lists to the specified length.
def randomize_lists(length):
    while True:
        # Shuffle list, get random choice, and append choice to username list.
        random.shuffle(CHARACTER_LIST)
        random_character = random.choice(CHARACTER_LIST)
        USERNAME.append(random_character)
        # Shuffle list, get random choice, and append  choice to password list.
        random.shuffle(CHARACTER_LIST)
        random_character = random.choice(CHARACTER_LIST)
        PASSWORD.append(random_character)
        # Stop the loop when the desired length is met.
        if len(USERNAME) and len(PASSWORD) == length:
            break
    # Return the username and password lists.
    return USERNAME, PASSWORD


# Display username and password as a string.
def show_results(username_list, password_list):
    # Empty strings for the username and password characters.
    username_string = ""
    password_string = ""
    # Print divider.
    print("=" * 25)
    # Loop through the username list.
    for character in username_list:
        # Concatenate character to username string.
        username_string += character
    # Print username string.
    print("Username:", username_string)
    # Loop through the password list
    for character in password_list:
        # Concatenate character to password string.
        password_string += character
    # Print password string.
    print("Password:", password_string)
    # Print a divider
    print("=" * 25)


# Group together the get length, randomize lists, and show results functions as the start randomizer function.
def start_randomizer():
    length = get_length()
    username, password = randomize_lists(length)
    show_results(username, password)


# Ask the user if they would like to end the program.
def end_randomizer():
    while True:
        # Prompt the user for input.
        user_input = input("Want to end the program? (y/n): ").lower()
        # End the program.
        if user_input == "y":
            #  Print goodbye message and end the program.
            print("See ya!")
            break
        # Clear the username and password lists and continue the program.
        elif user_input == "n":
            USERNAME.clear()
            PASSWORD.clear()
            # Print a divider
            print("=" * 25)
            start_randomizer()
        else:
            # Continue with the prompt if there is an invalid entry.
            print("Invalid entry. Try again.\n")
            continue


# The main program.
def main():
    display_intro()
    start_randomizer()
    end_randomizer()


if __name__ == "__main__":
    main()
