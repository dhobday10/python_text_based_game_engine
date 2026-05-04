from ui import ui_menu, yes_no, clear_screen, slowtype
import ui
import saves
from saves import SaveExists, NoSaveFound
import json, sys
import models


def title_screen():
    action = ui_menu(
                        [
                        ("New Game", new_game),
                        ("Load Save", load_save),
                        ("Exit", exit_game)
                        ],
                        title = "Resident Evil"
                        )
    return action[0]


def pre_game_menu_loop(function_to_run = None):
    function_to_run = title_screen()

    # runs until game is started
    while True:
        result = function_to_run()

        if callable(result):
            function_to_run = result
        else:
            break
    
    game_loop()
        

def game_loop():
    print("We've reached the game! What do we do now?")


def new_game():
    saves.init_index()
    while True:
        character = ui_menu([
            ("Chris Redfield", "Chris"),
            ("Jill Valentine", "Jill"),       
            ],
            title = "Select a Character",
            allow_back= True
            )
        
        if character[0] == "__BACK__":
            return title_screen

        while True: 
            difficulty = ui_menu([
                ("Like climbing a mountain.", "hard"),
                ("Like going on a hike.", "easy"),
                ("Like taking a walk.", "very_easy")
                ],
                allow_back= True)
            
            if difficulty[0] == "__BACK__":
                break
        
            player = models.Player.new_game(character, difficulty)
            game_state = models.GameState.new_game()
            return player, game_state


def load_save():
    save_data = prompt_for_existing_save()
    if callable(save_data):
        return save_data
    else:
        player = models.Player.load_save(save_data[0]['PLAYER_DATA'])
        game_state = models.GameState.load_save(save_data[1]['ROOMS'])
        return player, game_state

          
def prompt_for_existing_save(title = "Load Save"):
    index_path = saves.init_index()

    while True:
        with open(index_path, "r") as file:
            choice = ui_menu(json.load(file), title=title, allow_back= True)
            
            if choice[0] == "__BACK__":
                return title_screen
    
        try:
            return saves.validate_save(choice)
        except NoSaveFound:
            title = "No save data found in specified slot. Please select another slot or return to the title screen."
      

def exit_game():
    if yes_no("Quit the game?") == True:
        clear_screen()
        sys.exit()
    else:
        title_screen()   


def save_game(player, game_state):
    serialized_player, serialized_game_state = saves.save_serializer(player, game_state)
    serialized_save = (serialized_player, serialized_game_state)

    while True:
        INDEX = saves.init_index()
        with open(INDEX, "r") as file:
            choice = ui_menu(json.load(file), title = "Save Data", allow_back= True)
        
        if choice[0] == "__BACK__":
            return choice

        try:
            saves.write_save(choice, serialized_save, existing = False)
            break
        except SaveExists:
            if yes_no("There is already save data written to this slot. Would you like to overwrite it?"):
                saves.write_save(choice, serialized_save, existing = True)
                break
            
    saves.update_index(choice[1], player)


if __name__ == "__main__":
    pre_game_menu_loop()