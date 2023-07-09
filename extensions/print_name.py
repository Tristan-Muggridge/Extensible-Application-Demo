from models.extension import Extension
from models.state_manager import StateManager

def print_name(state: StateManager):
    state.get("name").subscribe(lambda value: print("print_name extension: age was changed to", value))
    
ext = Extension("print_name", print_name)