ROOM_DEFINITIONS = {
        "foyer_1F": {
            "name": "Foyer 1F",
            "description": "The foyer of the mansion",

            "exits": {
                "north": "central_stairway",
                "west": "dining_hall",
                "east": "statue_room"
            },

            "flags": {
                "intro_cutscene_seen": False,
                "returned_to_foyer_1F": False
            }
                    },  


        "dining_hall": {
            "name": "Dining Hall",
            "description": "A dimly lit dining hall, a grandfather clock ticks rythmically, the fireplace crackles faintly against the back wall.",

            "exits": {
                "east": "foyer_1F",
                "north": "dining_hall_hallway"
            },

            "flags": {
                "first_time_entering_cutscene_seen": False,
                "second_time_entering_cutscene_seen": False
            },

            "items": {
                "left": "ink_ribbon",
                "rear": "crest"
            },

            "interactables": {
                "Typewriter": "save_game"
            }
        }
    }

