from models.state_manager import StateManager

extensions_path = "extensions/"

def import_yaml(path: str):
    import yaml
    with open(path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def export_yaml(path: str, state: StateManager):
    import yaml

    data = {}
    for key in state.state:
        data[key] = state.state[key].get()

    with open(path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

def load_extensions(state: StateManager):
    print("-- Loading Extensions --")

    import os
    import importlib
    
    for filename in os.listdir(extensions_path):
        if filename.endswith(".py"):
            print(f"-- Loading {filename} --")
            module = importlib.import_module("extensions." + filename[:-3])
            module.ext.run(state)
    

if __name__ == "__main__":
    
    print("-- Setting up initial state --")

    store = StateManager()
    
    try: store.load_yaml(import_yaml("state.yaml"))
    except: pass

    store.set("name", "John")
    
    name = store.get("name")

    print("-- Initial State Initialised --\n")
    print(store)

    print()
    load_extensions(store)

    print("\n-- Extensions Loaded --\n")

    print("-- Setting age after extension load --\n")
    store.set("age", 30)
    age = store.get("age")

    print("-- Setting name to Jane --\n")
    name.set("Jane")

    print("\n-- Setting age to 31 --\n")
    store.set("age", 31)
    
    print("\n-- Ending State --")
    print(store)

    export_yaml("state.yaml", store)