from ui import slowtype, clear_screen
from definitions import ROOM_DEFINITIONS
from dialogue import DIALOGUE
from getpass import getpass

def foyer_intro(player, game_state):
    in_game_text(DIALOGUE["foyer_1F"]["foyer_intro"][player.character]) 
    move_player(player, "dining_hall")
    door_transition()


def door_transition():
    clear_screen()
    slowtype("You open the door....")
    

def dining_room_intro(player, game_state):
    in_game_text("You enter into a long room, split down the middle by a massive dining table. On the wall opposite you, a fireplace glows dimly. " \
                 "On the wall to your right, a grandfather clock ticks tirelessly.")


def move_player(player, destination = str):
    player.current_room = destination


def in_game_text(text):
    if not type(text) == list: # Converts a singular string to a list so that the following for statement does not attempt to parse a string character by character
        text = [text]

    for i in range(len(text)):
        print(text[i])
        getpass("\033[1;32m\nPress Enter to proceed.\033[0m\n")
        

EVENTS = {
    "foyer_intro": foyer_intro,
    "dining_hall_intro": dining_room_intro
}


def show_items():
    ...

def show_interactables():
    ...

def show_exits():
    ...

ACTION_HANDLER = {
    "items": show_items,
    "interactables": show_interactables,
    "exits": show_exits
}


def run_event(event_name, player, game_state):
    event_func = EVENTS[event_name]
    event_func(player, game_state)
