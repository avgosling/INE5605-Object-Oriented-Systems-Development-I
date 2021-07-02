from MVC.model.jogo import Jogo
from MVC.view.tela_jogo import TelaJogo

class ControladorJogo:
  def __init__(self, controlador_biblioteca):
      self.__controlador_biblioteca = controlador_biblioteca
      self.__tela = TelaJogo(self)
      self.__jogos = [age2, csgo, fifa20, dota2, f12020]

  def abre_tela(self):
    button, values = self.__tela.open()
    if button == 'Listar Jogos':
        self.listar_jogos()
    elif button == 'Pesquisar Jogo':
        self.pesquisar_jogo(values['nome'])
    elif button == 'Voltar ao menu principal':
        self.__controlador_biblioteca.abre_tela()

  def incluir_jogo(self, nome: str, genero: str, ano_lancamento: str, horas_jogadas: str, total_trofeus: str, preco: float):
    self.__jogos.append(Jogo(nome, genero, ano_lancamento, horas_jogadas, total_trofeus, preco))
    
  def excluir_jogo(self, nome: str):
    if isinstance (nome, str):
      for jogo in self.__jogos:
        if jogo.nome == nome:
          self.__jogos.remove(jogo)
          self.__tela.show_message("Jogos", "Jogo excluído com sucesso!")

  
  def listar_jogos(self):
        lista_jogos = ''
        for jogo in self.__jogos:
          lista_jogos += "Nome: " + jogo.nome + '\n' + "Ano do Lançamento: " + jogo.ano_lancamento + '\n' + "Gênero:" + jogo.genero + '\n' + "Preço: R$ " + str(jogo.preco) + '\n' + '\n'
        self.__tela.show_message('Jogos', lista_jogos)


  def listar_jogo_por_nome(self, nome: str):
      for jogo in self.__jogos:
        if jogo.nome == nome:
          return jogo

  def pesquisar_jogo(self, nome: str):
    try:
      jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(nome)
    except Exception:
      self.__tela.show_message('Erro', 'Jogo não encontrado na biblioteca.')
    else:
        self.__tela.show_message(jogo.nome, jogo.genero)
      
        


age2 = Jogo("Age of empires 2", "RTS", '1999', '0', '0', 50.00)
csgo = Jogo("Counter Strike GO", "FPS",'2012', '0', '0', 20.00)
fifa20 = Jogo("Fifa 20", "Esporte", '2019', '0', '0', 80.00)
dota2 = Jogo("Dota 2", "MOBA", '2013', '0', '0', 15.00)
f12020 = Jogo("Formula 1 2020", "Corrida", '2020', '0', '0', 90.00)