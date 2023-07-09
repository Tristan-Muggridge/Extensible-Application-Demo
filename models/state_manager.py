from models.state import State

class StateManager:
    def __init__(self):
        self.state = {}

    def get(self, key) -> State:
        try: 
            return self.state[key]
        except: 
            self.state[key] = State(None)
            return self.state[key]

    def set(self, key: str, value: State, listeners=[]) -> State:
        try:
            self.state[key].set(value)
        except: 
            self.state[key] = State(value, listeners)

        return self.state[key]

    def load_yaml(self, yaml):
        for key in yaml:
            self.set(key, yaml[key])
        return self

    def __str__(self) -> str:
        lines = []
        for key in self.state:
            lines.append(f"{key}: {self.state[key]}")
        
        return '\n'.join(lines)