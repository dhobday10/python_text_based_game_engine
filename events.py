def foyer_intro(player, game_state):
    print(f"The STARS members speak briefly, then split up. {player.character} enters the double doors on the left of the main foyer.")
    move_player(player, "dining_hall")


def dining_room_intro(player, game_state):
    print("You enter into a long room, split down the middle by a massive dining table. On the wall opposite you, a fireplace glows dimly. On the wall to your right, a grandfather clock ticks tirelessly.")


def move_player(player, destination = str):
    player.current_room = destination











EVENTS = {
    "foyer_intro": foyer_intro,
    "dining_hall_intro": dining_room_intro
}


def run_event(event_name, player, game_state):
    event_func = EVENTS[event_name]
    event_func(player, game_state)