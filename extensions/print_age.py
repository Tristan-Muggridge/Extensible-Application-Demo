from models.extension import Extension
from models.state_manager import StateManager

def print_age(state: StateManager):
    state.get("age").subscribe(lambda value: print("print_age extension: value was set to", value))
    
ext = Extension("print_age", print_age)