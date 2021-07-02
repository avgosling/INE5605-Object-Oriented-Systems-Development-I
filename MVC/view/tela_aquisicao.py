from MVC.view.tela import Tela
import PySimpleGUI as sg


class TelaAquisicao(Tela):

  def __init__(self, controlador_aquisicao):
    self.__controlador_aquisicao = controlador_aquisicao
    self.__window_menu = None
    self.__window_compra = None
    self.__window_historico = None

# # tratar quando o usuário não digitar nem 1,2,3 e opção 0 para voltar para o menu principal
  """
  def mostra_lista_str(self, lista: []):
        for elem in lista:
            print(elem)
  """
  """
  def mostrar_mensagem_de_erro(self, msg: str):
    print(msg)
  """

  def verifica_opcao(self, msg: str = "", opcoes_validas: [] = None):
    while True:
      valor_lido = input(msg)
      try:
        inteiro = int(valor_lido)
        if opcoes_validas and inteiro not in opcoes_validas:
          raise ValueError
        return inteiro
      except ValueError:
        self.show_message("Erro", "Digite uma opção válida.")

  def tratar_int_str(self, msg=""):
    while True:
      try:
        resposta = int(input(msg))
        return resposta
      except ValueError:
        self.show_message("Erro", "Resposta inválida. Verifique se está usando apenas números.")

  def tratar_float_str(self, msg=""):
    while True:
      try:
        resposta = float(input(msg))
        return resposta
      except ValueError:
        self.show_message("Resposta inválida. Verifique se está usando apenas números e se está usando ponto(exemplo 100.00).")
  
  def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

  def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_compra_jogo = [
                                [sg.Text('Compra Jogo')],
                                [sg.Text('Jogos Disponíveis')],
                                [sg.Text('1 - Age of empires 2')],
                                [sg.Text('R$50,00')],
                                [sg.Text('2 - Counter Strike Global Offensive')],
                                [sg.Text('R$20,00')],
                                [sg.Text('3 - Fifa 20')],
                                [sg.Text('R$80,00')],
                                [sg.Text('4 - Dota 2')],
                                [sg.Text('R$15,00')],
                                [sg.Text('5 - Formula 1 2020')],
                                [sg.Text('R$90,00')],
                                [sg.InputText('Digite o ID do Usuário', key='id_usuario')],
                                [sg.InputText('Digite a opção do jogo', key='opcao_jogo')],
                                [sg.Submit()]
                               ]

        layout_menu_aquisicao =[
                                [sg.Text('Clique em uma opção do menu abaixo:', size=(45, 1))],
                                [sg.Button('Comprar Jogo')],
                                [sg.Button('Histórico de compras')],
                                [sg.Button('Voltar ao menu Principal')]
                               ]
        
        layout_historico_aquisicao =[
                                [sg.Text('Historico de compras', size=(50, 500))],
                                [sg.Button('Voltar ao menu Principal')]
                               ]
        self.__window_menu = sg.Window('Menu de Aquisições').Layout(layout_menu_aquisicao)
        self.__window_compra = sg.Window('Comprar Jogo').Layout(layout_compra_jogo)
        self.__window_historico = sg.Window('Histórico de compras').Layout(layout_historico_aquisicao)

  def open(self):
    self.init_components()
    button, values = self.__window_menu.Read()
    if button == 'Comprar Jogo':
      button2, values = self.__window_compra.Read()
      self.close()
    elif button == 'Histórico de compras':
      return button, values
     
      self.close()
    self.close()
    return button, values

        
  
  def close(self):
      self.__window_menu.Close()
      self.__window_compra.Close()
      self.__window_historico.Close()
  
  """
  def tela_opcoes(self):
    print("----- AQUISIÇÕES -----")
    print("Escolha uma opção:")
    print("1: Comprar Jogo")
    print("2: Histórico de compras")
    print("0: Voltar ao menu principal")
    print("----------------------")
    opcao = self.verifica_opcao("Opção: ", [1,2,0])
    opcao_jogo = None
    id_usuario = None

    if opcao == 1:
      id_usuario = self.tratar_int_str("Insira o id do usuário: ")
      print("---- JOGOS DISPONIVÉIS ----")
      print("1: Age of empires 2  - R$50,00")
      print("2: Counter Strike Global Offensive - R$20,00")
      print("3: Fifa 20 - R$80,00")
      print("4: Dota 2  - R$15,00")
      print("5: Formula 1 2020 - R$90,00")
      print("0: Voltar")
      opcao_jogo = self.verifica_opcao("Opção: ", [1,2,3,4,5,0])
      return [opcao, id_usuario, opcao_jogo]

    elif opcao == 2:
      id_usuario = None
      opcao_jogo = None
      return [opcao, id_usuario, opcao_jogo]

    elif opcao == 0:
      id_usuario = None
      opcao_jogo = None
      return [opcao, id_usuario, opcao_jogo]

  def mostra_msg_de_erro(self, msg: str):
    print(msg)
  """
