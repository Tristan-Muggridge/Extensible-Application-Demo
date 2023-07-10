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
    # 供給されるデータの初期化
    store = StateManager()
    
    # 既存のデータを読み込む
    try: store.load_yaml(import_yaml("state.yaml"))
    except: pass

    # Nameというキーに対して、初期値を設定する
    store.set("name", "John")
    name = store.get("name")

    # Nameが設定されたうえで、供給のデータを表示する
    print("-- Initial State Initialised --\n")
    print(store)

    print()

    # ダウンロードした拡張機能をロードする
    load_extensions(store)

    print("\n-- Extensions Loaded --\n")

    print("-- Setting age after extension load --\n")
    
    # 拡張機能をロードした後に、ageを設定する
    store.set("age", 30)
    age = store.get("age")

    print("-- Setting name to Jane --\n")
    # NameをJaneに変更する
    name.set("Jane")

    print("\n-- Setting age to 31 --\n")
    # Ageを31に変更する
    store.set("age", 31)
    
    print("\n-- Ending State --")

    # 最後に、最終的な状態を表示する
    print(store)

    # 最終的な状態を保存する
    export_yaml("state.yaml", store)