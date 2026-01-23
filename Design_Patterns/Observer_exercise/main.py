from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, status):
        pass
    
class Pedido:
    def __init__(self):
        self._observers = []
        self._status = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._status)

    def set_status(self, status):
        self._status = status
        print(f"\nStatus alterado para: {status}")
        self.notify()
    
class EmailNotifier(Observer):
    def update(self, status):
        print(f"Email enviado: Pedido {status}")   

class LogNotifier(Observer):
    def update(self, status):
        print(f"Log registrado: Pedido {status}")
        
class SMSNotifier(Observer):
    def update(self, status):
        print(f"SMS enviado: Pedido {status}")
         

pedido = Pedido()

email = EmailNotifier()
sms = SMSNotifier()
log = LogNotifier()

pedido.attach(email)
pedido.attach(sms)
pedido.attach(log)

pedido.set_status("ENVIADO")