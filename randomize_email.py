#!/usr/bin/env python3

"""Generates two random sets of strings. The length of the strings are determined by the user. The character set
includes lower (i.e., abc...xyz) and uppercase (i.e., ABC...XYZ) letters and numbers (i.e., 0-9). The purpose of this
program is to automate online character randomizers on a local machine. This increases privacy by reducing online
exposure. This program is meant to be used for creating a username and password for a throw away email. For example,
Bob wants to create a throw away email address. He can access Gmail through Tor, run this program to generate a random
username and password, and copy and paste each string into the respective fields. Bob can then do what he likes with
the string sets. He may delete them or save them in a txt file for later use, like so:

randomThrowAwayEmail.txt
Email:w2rvRfSfPaezU9C@gmail.com
Username: w2rvRfSfPaezU9C
Password: a0XW8msX54X1w9o
"""

# Import the random module.
import random
import tkinter as tk
from tkinter import ttk

# A list of lower (i.e., abc...xyz) and uppercase (i.e., ABC...XYZ) letters and numbers (i.e., 0-9).
CHARACTER_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Empty lists for the output.
USERNAME = []
PASSWORD = []


# Prompt the user to select the length of username/password.
def get_length():
    while True:
        try:
            length = int(input('How many random characters would you like to generate?: '))
            if length == 0:
                print("Pick a number greater than zero.\n")
                continue
        except ValueError:
            print("Invalid entry. Try again.\n")
        else:
            return length


# Select a random set of characters and numbers of the desired length.
# Set stop_loop Boolean to False.
def start_randomizing(length):
    stop_loop = False
    # Start loop.
    while not stop_loop:
        # Shuffle list, get random choice, and append to username.
        random.shuffle(CHARACTER_LIST)
        random_character = random.choice(CHARACTER_LIST)
        USERNAME.append(random_character)

        # Shuffle list, get random choice, and append to password.
        random.shuffle(CHARACTER_LIST)
        random_character = random.choice(CHARACTER_LIST)
        PASSWORD.append(random_character)
        # Stop the loop when the desired length is met.
        if len(USERNAME) and len(PASSWORD) == length:
            stop_loop = True
    return USERNAME, PASSWORD


def print_results(username, password):
    # Print randomized username and password.
    print("Username:")
    for character in username:
        print(character, end='')
    # Print on new line.
    print()
    print("Password:")
    for character in password:
        print(character, end='')


# GUI section
def get_root():
    root = tk.Tk()
    root.title("Random Username and Password Generator")
    root.geometry("500x150")
    return root


def get_frame(root):
    frame = ttk.Frame(root,
                      padding="10 10 10 10")
    frame.pack(fill=tk.BOTH,
               expand=True)
    return frame


def show_label(frame):
    ttk.Label(frame,
              text="How many random characters would you like to generate?").pack()


def get_entry(frame):
    entry = tk.StringVar()
    user_entry = ttk.Entry(frame,
                           width=25,
                           textvariable=entry)
    length = user_entry.get()
    user_entry.pack()
    return length


def show_username(frame):
    username_text = tk.StringVar()
    username_entry = ttk.Entry(frame,
                               width=25,
                               textvariable=username_text,
                               state="readonly")
    username = username_entry.get()
    username_entry.pack()
    return username


def show_password(frame):
    password_text = tk.StringVar()
    password_entry = ttk.Entry(frame,
                               width=25,
                               textvariable=password_text,
                               state="readonly")
    password = password_entry.get()
    password_entry.pack()
    return password


def show_button(frame):
    generate_button = ttk.Button(frame,
                                 text="Generate")  # command=?
    generate_button.pack()


def start_mainloop(root):
    root.mainloop()


# set up the tkinter with a length field, two display text fields, and a button to generate results
def main():

    length = get_length()
    username, password = start_randomizing(length)
    print_results(username, password)

    # root = get_root()
    # frame = get_frame(root)
    # show_label(frame)
    # length = get_entry(frame)
    #
    # show_button(frame)
    # username = show_username(frame)
    # password = show_password(frame)
    # start_mainloop(root)


if __name__ == "__main__":
    main()

# save it as exe file
