class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    def get_rua(self):
        return self.__rua

    def set_rua(self, rua):
        self.__rua = rua

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_bairro(self):
        return self.__bairro

    def set_bairro(self, bairro):
        self.__bairro = bairro

    def get_cidade(self):
        return self.__cidade

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_cep(self):
        return self.__cep

    def set_cep(self, cep):
        self.__cep = cep

