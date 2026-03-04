from time import sleep
from os import name, system
from pathlib import Path
import sys, json

class Savedata:
    def __init__(self, character, difficulty, new=False):
        self.character = character
        self.difficulty = difficulty


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

def init_index(max_slots= 8):
    save_dir = Path('SAVEDATA')
    save_dir.mkdir(parents= True, exist_ok=True)
    INDEX = save_dir / "index.json"

    if not INDEX.exists():
        save = []
        for i in range(max_slots):
            save.append(("Empty Slot", f"slot_{i}"))
        with open(INDEX, "w") as file:
            json.dump(save, file, indent=4)
    
    return INDEX
    
    
        
        


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def validate(options, max):
    while True:
        prompt = input("")
        for option in range(1, max + 1):
            if str(option) == prompt:
                return (options[option-1][1])
            
        print("Invalid Choice")


def ui_menu(options, title = ''):
    clear_screen()

    if title != '':
        print(title)

    for _, opt in enumerate(options, start = 1):
        print(f"{_}. {opt[0]}")
    
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


def new_game():
    init_index()
    character, difficulty = ui_menu([
                        ("Chris Redfield", "Chris"),
                        ("Jill Valentine", "Jill"),       
                        ],
                        title = "Select a Character"

                        ),  ui_menu([
                        ("Like climbing a mountain.", "hard"),
                        ("Like going on a hike.", "easy"),
                        ("Like taking a walk.", "very_easy")
                        ])
    player = Savedata(character, difficulty, new = True)
                           
    

def load_save():
    INDEX = init_index()
    with open(INDEX, "r") as file:
       choice = ui_menu(json.load(file), title = "Save Data")
    
    print(choice)
    
    
def exit_game():
    if yes_no("Quit the game?") == True:
        clear_screen()
        sys.exit()
    else:
        title_screen()          


def title_screen():
    action = ui_menu(
                        [
                        ("New Game", new_game),
                        ("Load Save", load_save),
                        ("Exit", exit_game)
                        ],
                        title = "Resident Evil"
                        )
    
    action()
    

def main(save):
    ...


if __name__ == "__main__":
    title_screen()