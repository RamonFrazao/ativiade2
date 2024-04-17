from Disciplina import Disciplina
from Professor import Professor


class Curso:
    def __init__(self, nome, codigo):
        self.__nome = nome
        self.__codigo = codigo
        self.__disciplinas = []
        self.__professores = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def addDisciplina(self, nome, codigo):
        self.__disciplinas.append(Disciplina(nome, codigo))

    def addProfessor(self, nome, matricula):
        self.__professores.append(Professor(nome, matricula))
