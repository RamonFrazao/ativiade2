from Endereco import Endereco


class Professor:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__endereco = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def addEndereco(self, rua, numero, bairro, cidade, estado, cep):
        self.__endereco.append(Endereco(rua, numero, bairro, cidade, estado, cep))
