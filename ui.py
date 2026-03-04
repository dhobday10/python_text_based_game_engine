from time import sleep
from os import name, system
import sys

def validate(options, max):
    while True:
        prompt = input("")
        for option in range(1, max + 1):
            if str(option) == prompt:
                return (options[option-1][1], option)
            
        print("Invalid Choice")


def ui_menu(options, title = ''):
    clear_screen()

    if title != '':
        print(title)

    for num, opt in enumerate(options, start = 1):
        print(f"{num}. {opt[0]}")
    
    return validate(options, len(options))


def yes_no(question): 
    acceptable_yes = ["yes", "y"]
    acceptable_no = ["no", "n"]
    clear_screen()
    print(f"{question} (yes/no)")

    while True:
        answer = input('').strip().lower()
        if answer in acceptable_yes:
            return True
        elif answer in acceptable_no:
            return False
        
        print("Invalid Choice")

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def slowtype(text):
    clear_screen()
    for char in text:
        if char == ".":
            sleep(0.15)
            sys.stdout.write(char)
        else:    
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.15)
    print()