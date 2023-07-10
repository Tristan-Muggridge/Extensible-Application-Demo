from models.extension import Extension
from models.state_manager import StateManager

def print_age(state: StateManager):
    """
        This extension prints the age whenever it is changed.
        この拡張機能は、年齢が変更されるたびに年齢を表示します。
    """
    state.get("age").subscribe(lambda value: print("print_age extension: value was set to", value))
    try:
        state.set("age_changes", state.get("age_changes").get() + 1)
    except:
        state.set("age_changes", 1)
    
ext = Extension("print_age", print_age)