import definitions

class Player:
    def __init__(self, character, difficulty, current_room, hp, inventory, flags):
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
                   [], 
                   {}
                   )
    

    @classmethod
    def load_save(cls, save_dict):
        return cls(
                    save_dict["character"],
                    save_dict["difficulty"],
                    save_dict["location"],
                    save_dict["health"],
                    [],
                    {} # Save game needs to be reconfirgured to write inventory and flags, using a blank list and dict respectively for now
                    )

    
    def to_dict(self):
        player_status = {
            "Character": self.character,
            "difficulty": self.difficulty,
            "location": self.location,
            "health": self.health 
        }

        #Flags section will be moved to GameState class eventually
        flags = {
            "hallway_cutscene": self.hallway_cutscene_seen,
            "dining_hall_cutscene": self.dining_hall_cutscene_seen 
        }
        return (player_status, flags)


class GameState():
    def __init__(self, room_states, global_flags): # for now, global flags does nothing
        self.roomstates = room_states

    @classmethod
    def new_game(cls):
        room_states = { 
            "foyer_1F": {
                "items": {
                    "ink_ribbon": {
                        "taken": False,
                        "Quantity": 1
                    }
                },
                "actions": {
                    "Use Typewriter": "save_game",
                    "Go to Dining Hall": "enter_room",
                    "Go up the Stairs": "climb_stairs"
                },
                "flags": {
                    "intro_cutscene_seen_foyer_1F": False
                }
            },

            "dining_hall_1F": {}
        }

        return cls(room_states)
    
    @classmethod
    def load_save(cls, save_dict):
        print(save_dict)