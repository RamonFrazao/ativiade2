from Curso import Curso
from Endereco import Endereco


class Aluno:
    def __init__ (self, nome, dataNascimento, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__dataNascimento = dataNascimento
        self.__curso = []
        self.__endereco = []

    def get_nome (self):
        return self.__nome

    def set_nome (self, nome):
        self.__nome = nome

    def get_matricula (self):
        return self.__matricula

    def set_matricula (self, matricula):
        self.__matricula = matricula

    def get_data_nascimento (self):
        return self.__dataNascimento

    def set_dataNascimento (self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def get_curso (self):
        return self.__curso

    def set_curso (self, curso):
        self.__curso = curso

    def get_endereco (self):
        return self.__endereco

    def set_endereco (self, endereco):
        self.__endereco = endereco

    def addEndereco(self, rua, numero, bairro, cidade, estado, cep):
        self.__endereco.append(Endereco(rua, numero, bairro, cidade, estado, cep))

    def addCurso(self, nome, codigo):
        self.__curso.append(Curso(nome, codigo))