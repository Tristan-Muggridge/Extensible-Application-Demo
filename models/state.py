from models.emitter import Emitter

class State(Emitter):
    def __init__(self, value, listeners=[]):
        self.value = value
        self.listeners = listeners
            
    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value
        self.emit(value)

    def __str__(self) -> str:
        return str(self.value)
