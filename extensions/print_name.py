from models.extension import Extension
from models.state_manager import StateManager

def print_name(state: StateManager):
    """
        This extension prints the name whenever it is changed.
        この拡張機能は、名前が変更されるたびに名前を表示します。
    """
    state.get("name").subscribe(lambda value: print("print_name extension: age was changed to", value))
    try:
        state.set("name_changes", state.get("name_changes").get() + 1)
    except:
        state.set("name_changes", 1)

ext = Extension("print_name", print_name)