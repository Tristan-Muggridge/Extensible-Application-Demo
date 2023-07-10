from models.state import State

class StateManager:
    """
        This class manages the state of the application.\n
        このクラスは、アプリケーションの状態を管理します。
    """
    def __init__(self):
        self.state = {}

    def get(self, key) -> State:
        """
            This method returns the state of the given key.\n
            このメソッドは、指定されたキーの状態を返します。
        """
        try: 
            return self.state[key]
        except: 
            self.state[key] = State(None)
            return self.state[key]

    def set(self, key: str, value: State, listeners=[]) -> State:
        """
            This method sets the state of the given key.\n
            このメソッドは、指定されたキーの状態を設定します。
        """
        try:
            self.state[key].set(value)
        except: 
            self.state[key] = State(value, listeners)

        return self.state[key]

    def load_yaml(self, yaml):
        """
            This method loads the state from a yaml file.\n
            このメソッドは、yamlファイルから状態をロードします。
        """
        for key in yaml:
            self.set(key, yaml[key])
        return self

    def __str__(self) -> str:
        lines = []
        for key in self.state:
            lines.append(f"{key}: {self.state[key]}")
        
        return '\n'.join(lines)