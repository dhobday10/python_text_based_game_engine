import saves
import main

class Player:
    def __init__(self, character, difficulty, new=False):
        # Player attributes
        self.character = character
        self.difficulty = difficulty
        self.location = "placeholder"
        self.health = 100
        
        # Flags
        self.hallway_cutscene = 0
        self.dining_hall_cutscene = 0
    
    def to_dict(self):
        player_status = {
            "Character": self.character,
            "difficulty": self.difficulty,
            "location": self.location,
            "health": self.health 
        }

        flags = {
            "hallway_cutscene": self.hallway_cutscene,
            "dining_hall_cutscene": self.dining_hall_cutscene
        }   
        return (player_status, flags)


player = Player("Jill", "hard")

main.load_save()

