class Usuario:

    def __init__(self, nome: str, email: str, id_usuario: str, saldo: float, jogos_adquiridos:[]):
    #    if isinstance((nome, str) and (email, str) and (id_usuario, str)):
            self.__nome = nome
            self.__email = email
            self.__id_usuario = id_usuario
            self.__aquisicoes = []
            self.__usuarios = []
            self.__saldo = saldo
            self.__jogos_adquiridos = []
        
    @property
    def nome(self):
      return self.__nome

    @nome.setter
    def nome(self, nome:str):
      if isinstance(nome, str):
        self.__nome = nome

    @property
    def email(self):
      return self.__email

    @email.setter
    def email(self, email:str):
      if isinstance(email,str):
        self.__email = email

    @property
    def id_usuario(self):
      return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario: str):
      if isinstance(id_usuario,str):
        self.__id_usuario = id_usuario

    @property
    def aquisicoes(self):
      return self.__aquisicoes
    
    @property
    def usuarios(self):
     return self.__usuarios
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo: float):
        self.__saldo = novo_saldo
    
    @property
    def jogos_adquiridos(self):
      return self.__jogos_adquiridos
    
    @jogos_adquiridos.setter
    def jogos_adquiridos(self, jogos_adquiridos:[]):
      self.__jogos_adquiridos = jogos_adquiridos