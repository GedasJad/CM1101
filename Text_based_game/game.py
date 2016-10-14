#!/usr/bin/python3

from map import rooms
import string
import re
from string import ascii_letters, digits


def remove_punct(text):
        for c in string.punctuation:
            text=text.replace(c,"")
            return text
    
    
    
def remove_spaces(text):
    return text.strip(" ")


def normalise_input(user_input):
    user_input=remove_punct(user_input)
    user_input=remove_spaces(user_input)
    return user_input.lower()

    
def display_room(room):
    print (" ")
    print (room["name"].upper())
    print (" ")
    print (room["description"])
    print (" ")
    
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_menu_line(direction, leads_to):
    print ("Go " +direction.upper()+ " to " + leads_to + ".")
    


def print_menu(exits):
    print("You can:")
    for key in exits:
        print_menu_line(key, exit_leads_to(exits, key))
    print("Where do you want to go?")


def is_valid_exit(exits, user_input):
    for key in exits:
        if(key==user_input):
            return True
    return False


def menu(exits):
    while True:
        print_menu(exits)
        user_input=normalise_input(input())
        if (is_valid_exit(exits, user_input)==True):
            return user_input

def move(exits, direction):
    return rooms[exits[direction]]


def main():
    current_room = rooms["Reception"]

    while True:
        display_room(current_room)

        exits = current_room["exits"]

        direction = menu(exits)

        current_room = move(exits, direction)

if __name__ == "__main__":
    main()
