class Jogo:

    def __init__(self, nome: str, genero: str, ano_lancamento: str, horas_jogadas: str, total_trofeus: str, preco: str):
            self.__genero = genero
            self.__nome = nome
            self.__ano_lancamento = ano_lancamento
            self.__horas_jogadas = horas_jogadas
            self.__total_trofeus = total_trofeus
            self.__jogos = []
            self.__preco = preco

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
      if isinstance(genero, str):
        self.__genero = genero

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
      if isinstance(nome, str):
        self.__nome = nome

    @property
    def ano_lancamento(self):
        return self.__ano_lancamento

    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento: str):
      if isinstance(ano_lancamento, str):
        self.__ano_lancamento = ano_lancamento

    @property
    def horas_jogadas(self):
        return self.__horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, horas_jogadas: str):
      if isinstance(horas_jogadas, str):
        self.__horas_jogadas = horas_jogadas
    
    @property
    def total_trofeus(self):
        return self.__total_trofeus

    @total_trofeus.setter
    def total_trofeus(self, total_trofeus: str):
      if isinstance(total_trofeus, str):
        self.__total_trofeus = total_trofeus

    @property
    def jogos(self):
     return self.__jogos

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: str):
      self.__preco = novo_preco