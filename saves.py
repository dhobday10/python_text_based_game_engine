import json
import models
from pathlib import Path

class SaveExists(Exception):
    """Exception raised when user attempts to write over an existing save"""

def init_index(max_slots= 8):
    save_dir = Path('SAVEDATA')
    save_dir.mkdir(parents= True, exist_ok=True)
    INDEX = save_dir / "index.json"

    if not INDEX.exists():
        save = []
        for i in range(max_slots):
            save.append(("Empty Slot", f"save_{i}"))
        with open(INDEX, "w") as file:
            json.dump(save, file, indent=4)
    
    return INDEX


def save_serializer(raw):
    # exists solely to catch the player save's current status and convert it to json
    return raw.to_dict()


def get_save(save_num):
    save_dir = Path(f'SAVEDATA/{save_num[0]}{save_num[1]}.json')    

    if save_dir.exists():
        return save_dir
    else:
        return False
    


def save_deserializer(save_num):
    ...
    
 
def write_save(slot, save_json, existing = False):
    save_dir = Path('SAVEDATA')
    save_file = save_dir / f"save_0{slot[1]}.json"
    
    if save_file.exists() and existing == False:
        raise SaveExists()
    
    with open(save_file, "w") as file:
        json.dump(save_json, file, indent = 4)


def update_index(slot, data):
    # Below code updates the list of saves the player sees
    INDEX = init_index()
    with open(INDEX, "r") as file:
        save_slots = json.load(file)
    
    
    save_slots[slot-1][0] = f"{data.character} {data.difficulty}"

    with open(INDEX, "w") as file:
        json.dump(save_slots, file, indent = 4)

    
    
    

        
    
