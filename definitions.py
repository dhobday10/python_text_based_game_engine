# static elements for each room

ROOM_DEFINITIONS = {
        "foyer_1F": {
            "name": "Foyer 1F",
            "description": "The foyer of the mansion",

            "exits": {
                "north": "central_stairway",
                "west": "dining_hall",
                "east": "statue_room"
                    }
                    },  


        "dining_hall": {
            "name": "Dining Hall",
            "description": "A dimly lit dining hall, a grandfather clock ticks rythmically, the fireplace crackles faintly against the back wall.",

            "exits": {
                "east": "foyer_1F",
                "north": "dining_hall_hallway"
                     },

            "items": {
                "left": "ink_ribbon",
                "rear": "crest"
                     },

            "interactables": {
                ...
                    }
        }
    }

