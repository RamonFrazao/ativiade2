from Curso import Curso
from Professor import Professor
from Sala import Sala


class Disciplina:
    def __init__ (self, nome, codigo):
        self.__nome = nome
        self.__codigo = codigo
        self.__professor = []
        self.__sala = []
        self.__curso = []

    def get_nome (self):
        return self.__nome

    def set_nome (self, nome):
        self.__nome = nome

    def get_codigo (self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def addSala(self, numero, capacidade, localizacao):
        self.__sala.append(Sala(numero, capacidade, localizacao))

    def addCurso(self, nome, codigo):
        self.__sala.append(Curso(nome, codigo))

    def addProfessor(self, nome, matricula):
        self.__professor.append(Professor(nome, matricula))