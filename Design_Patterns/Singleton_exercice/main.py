# Maneira correta de criar um objeto com o design pattern Singleton
# Singleton é sobre impedir criação.
# Quem impede criação em Python é o __new__, não o __init__

class AppConfig:
    '''Criação da configuração de ambiente'''
    _instance = None

    def __new__(cls, name, environment): # Controla se um novo objeto será criado ou não
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.environment = environment
        return cls._instance


config1 = AppConfig("Minha App", "dev")
config2 = AppConfig("Outra App", "prod")

print(config1 is config2)              # True
print(config1.name)                    # Minha App
print(config2.name)                    # Minha App
print(config2.environment)             # dev

