from models.extension import Extension

class Emitter:
    """
        This class represents an emitter which may be subscribed to. Upon update of the value all subscribers will have their registered functions run.\n
        このクラスは、購読できるエミッターを表します。値が更新されると、すべての購読者の登録された関数が実行されます。
    """
    def __init__(self):
        self.listeners = []
    
    def subscribe(self, pckg: Extension):
        """
            This method subscribes to the emitter.\n
            このメソッドは、エミッターに購読します。
        """
        self.listeners.append(pckg)

    def unsubscribe(self, pckg: Extension):
        """ 
            This method unsubscribes from the emitter.\n
            このメソッドは、エミッターから購読を解除します。
        """
        self.listeners.remove(pckg)

    def emit(self, *args, **kwargs):
        """
            This method emits the value to all subscribers.\n
            このメソッドは、値をすべての購読者に送信します。
        """
        print(f"Emitting {len(self.listeners)} callbacks")
        for callback in self.listeners:
            callback(*args, **kwargs)