import definitions

class Player:
    def __init__(self, character, difficulty, current_room, hp, inventory):
        self.character = character
        self.difficulty = difficulty
        self.current_room = current_room
        self.hp = hp
        self.inventory = inventory


    @classmethod
    def new_game(cls, character, difficulty):
        return cls(character, 
                   difficulty, 
                   "foyer_1F", 
                   100, 
                   inventory = [], 
                   )
    

    @classmethod
    def load_save(cls, save_dict):
        return cls(
                    save_dict["character"],
                    save_dict["difficulty"],
                    save_dict["current_room"],
                    save_dict["hp"],
                    inventory = []
                    )

    
    def to_dict(self):
        player_status = {
            "PLAYER_DATA": {
            "character": self.character,
            "difficulty": self.difficulty,
            "current_room": self.current_room,
            "hp": self.hp,
            "inventory": self.inventory
            }
        }


        return (player_status)


class GameState():
    def __init__(self, room_states, global_flags): # for now, global flags does nothing
        self.roomstates = room_states


    @classmethod
    def new_game(cls):
        room_states = {}
        for room, room_state in definitions.ROOM_DEFINITIONS.items():
            room_states[room] = {
                "flags": {},
                "items_taken": []
            }

        return cls(room_states, {})
    
    
    @classmethod
    def load_save(cls, save_dict):
        return cls(save_dict, {})


    def to_dict(self):
        room_states_to_save = {}

        room_states_to_save["ROOMS"] = {}
        for room, room_state in self.roomstates.items():
            room_states_to_save["ROOMS"][room] = {
                "flags": room_state["flags"],
                "items_taken": room_state["items_taken"]
            }
        
        return room_states_to_save




   

