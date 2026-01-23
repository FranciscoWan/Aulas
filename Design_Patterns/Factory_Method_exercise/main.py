from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, massage:str):
        pass

class EmailNotification(Notification):
    def send(self, massage:str):
        return f"Enviando EMAIL: {massage}"

class SMSNotification(Notification):
    def send(self, massage:str):
        return f"Enviando SMS: {massage}"

class PushNotification(Notification):
    def send(self, massage:str):
        return f"Enviando mensagem PUSH: {massage}"
    
class NotificationFactory:
    @staticmethod
    def create_notification(type: str) -> Notification:
        if type == "email":
            return EmailNotification()
        elif type == "sms":
            return SMSNotification()
        elif type == "push":
            return PushNotification()


factory = NotificationFactory()

notification = factory.create_notification("email")
print(notification.send("olá"))


# Importante: eles resolvem problemas diferentes
# @staticmethod → organização e intenção
# @abstractmethod → contrato e segurança


# Factory que não guarda estado → @staticmethod
# Factory que guarda configuração → método com self
