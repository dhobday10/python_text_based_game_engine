ROOM_DEFINITIONS = {
        "foyer_1F": {
            "name": "Foyer 1F",
            "description": "The foyer of the mansion",

            "exits": {
                "north": "central_stairway",
                "west": "dining_hall",
                "east": "statue_room"
            },

            "events": {
                "on_first_enter": "foyer_intro",
            },

            "items": {
                "ink_ribbon": 2
            },

            "interactables": {
                "typewriter"
            }
                    },  
                
            


        "dining_hall": {
            "name": "Dining Hall",
            "description": "A dimly lit dining hall, a grandfather clock ticks rythmically, the fireplace crackles faintly against the back wall.",

            "events": {
                "on_first_enter": "dining_hall_intro",
            },

            "actions": {

                "items": {
                    "action_description": "Scan the room for useful items",

                    "default_contents": {
                        "ink_ribbon": "Ink Ribbon",
                        "fireplace_crest": "Fireplace Crest"
                    },

                    "quantities": {
                        "ink_ribbon": 3,
                        "fireplace_crest": 1
                    }
                },

                "interactables": {
                    "action_description": "Look for anything you can interact with",
                    "Typewriter": "save_game"
                },

                "exits": {
                    "action_description": "Search for exit routes",
                    "east": "foyer_1F",
                    "north": "dining_hall_hallway"
                }
            
            }
        }
    }
