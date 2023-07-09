from models.callback import Callback

class Emitter:
    def __init__(self):
        self.listeners = []
    
    def subscribe(self, pckg: Callback):
        self.listeners.append(pckg)

    def unsubscribe(self, callback):
        self.listeners.remove(callback)

    def emit(self, *args, **kwargs):
        print(f"Emitting {len(self.listeners)} callbacks")
        for callback in self.listeners:
            callback(*args, **kwargs)