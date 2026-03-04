from os import name, system
from time import sleep
import sys

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