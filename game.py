import ui, models, events, definitions
from events import run_event

def game_loop(player_obj, game_state_obj):
    while True:
        room_id = player_obj.get_room()                     # Current Room
        room_state = game_state_obj.room_states[room_id]    # Current status of the room based on the save data
        room_def = definitions.ROOM_DEFINITIONS[room_id]    # Static room definitions 

        first_enter_event = room_def["events"].get("on_first_enter")
        

        if first_enter_event and first_enter_event not in room_state["flags"]:
            run_event(first_enter_event, player_obj, game_state_obj)
            room_state["flags"][first_enter_event] = 1
            continue

        get_options(room_def)
        
def get_options(room_def):
    ...
           
        
        
