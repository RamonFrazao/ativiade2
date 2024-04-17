class Sala:
    def __init__(self, numero, capacidade, localizacao):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__localizacao = localizacao

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def get_localizacao(self):
        return self.__localizacao

    def set_localizacao(self, localizacao):
        self.__localizacao = localizacao
