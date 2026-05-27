import ui, models, events
from definitions import ROOM_DEFINITIONS
from events import run_event, ACTION_HANDLER

def game_loop(player_obj, game_state_obj):
    while True:
        ui.clear_screen()
        room_id = player_obj.get_room()                     # Current Room
        room_state = game_state_obj.room_states[room_id]    # Current status of the room based on the save data
        room_def = ROOM_DEFINITIONS[room_id]                # Static room definitions 

        first_enter_event = room_def["events"].get("on_first_enter")
        if first_enter_event and first_enter_event not in room_state["flags"]:
            run_event(first_enter_event, player_obj, game_state_obj)
            room_state["flags"][first_enter_event] = 1
            continue
        
        actions = get_actions(room_id)
        choice = ui.ui_menu(actions, title = "What do you do?")
        

        
def get_actions(room_id):
    actions = []

    for action in ROOM_DEFINITIONS[room_id]["actions"]:
        actions.append((ROOM_DEFINITIONS[room_id]["actions"][action]["action_description"], action))

    return actions

    
           
        
        
