import definitions

class Player:
    def __init__(self, character, difficulty, new=False, save_data = None):
        # Player attributes
        if new == True:
            self.character = character
            self.difficulty = difficulty
            self.location = "placeholder"
            self.health = 100
        
        # Global Flags
        self.hallway_cutscene_seen = 0
        self.dining_hall_cutscene_seen = 0

    
    def to_dict(self):
        player_status = {
            "Character": self.character,
            "difficulty": self.difficulty,
            "location": self.location,
            "health": self.health 
        }

        flags = {
            "hallway_cutscene": self.hallway_cutscene_seen,
            "dining_hall_cutscene": self.dining_hall_cutscene_seen
        }
        return (player_status, flags)