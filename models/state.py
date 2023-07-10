from models.emitter import Emitter

class State(Emitter):
    """
        This class represents a state.\n
        このクラスは、状態を表します。
    """
    def __init__(self, value, listeners=[]):
        self.value = value
        self.listeners = listeners
            
    def get(self):
        """
            This method returns the value of the state.\n
            このメソッドは、状態の値を返します。
        """
        return self.value
    
    def set(self, value):
        """
            This method sets the value of the state.\n
            このメソッドは、状態の値を設定します。
        """
        self.value = value
        self.emit(value)

    def __str__(self) -> str:
        return str(self.value)
