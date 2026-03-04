from ui import ui_menu, yes_no, clear_screen, slowtype
import saves
from saves import SaveExists
import json, sys


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


def new_game():
    saves.init_index()
    character = ui_menu([
                        ("Chris Redfield", "Chris"),
                        ("Jill Valentine", "Jill"),       
                        ],
                        title = "Select a Character"

                        )
    difficulty = ui_menu([
                        ("Like climbing a mountain.", "hard"),
                        ("Like going on a hike.", "easy"),
                        ("Like taking a walk.", "very_easy")
                        ])
    
    player = saves.models.Player([character, difficulty, True])
   

def load_save():
    INDEX = saves.init_index()
    with open(INDEX, "r") as file:
       choice = ui_menu(json.load(file), title = "Save Data")
    
    print(choice)


def exit_game():
    if yes_no("Quit the game?") == True:
        clear_screen()
        sys.exit()
    else:
        title_screen()   

def save_game(raw_object):
    serialized = saves.save_serializer(raw_object)

    INDEX = saves.init_index()
    with open(INDEX, "r") as file:
       choice = ui_menu(json.load(file), title = "Save Data")
    
    try:
        saves.write_save(choice, serialized, existing = False)
    except SaveExists:
        if yes_no("There is already save data written to this slot. Would you like to overwrite it?"):
            saves.write_save(choice, serialized, existing = True)
        else:
            save_game()


    saves.update_index(choice[1], raw_object)


def main(save):

    ...


if __name__ == "__main__":
    title_screen()