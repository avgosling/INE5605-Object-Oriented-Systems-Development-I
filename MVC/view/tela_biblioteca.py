from MVC.view.tela import Tela
import PySimpleGUI as sg

class TelaBiblioteca(Tela):
    def __init__(self, controlador_biblioteca):
        self.controlador_biblioteca = controlador_biblioteca
        self.__window = None
        self.__hide = False

    def verifica_opcao(self, msg: str = "", opcoes_validas: [] = None):
        while True:
            valor_lido = input(msg)
            try:
                inteiro = int(valor_lido)
                if opcoes_validas and inteiro not in opcoes_validas:
                    raise ValueError
                return inteiro
            except ValueError:
              sg.Popup("Digite uma opção válida.")
                #if opcoes_validas:
                #   print("Opções válidas: ", opcoes_validas)
    def init_components(self):
      sg.ChangeLookAndFeel('SandyBeach')
      layout_menu_biblioteca = [
            [sg.Text('Clique na opção desejada')],
            [sg.Button('Usuários')],
            [sg.Button('Jogos')],
            [sg.Button('Aquisições')],
            [sg.Button('Sair')],
            ]
      self.__window = sg.Window('Menu da Biblioteca').layout(layout_menu_biblioteca)

    def open(self):
        self.init_components()
        button, values = self.__window.read()
        self.close()
        return button, values

    def close(self):
        self.__window.close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    # tem que adicionar o super().  em cada tela  - André
    # tratar quando o usuário não digitar nem 1,2,3
    # esta é a primeira tela que o usuário vê quando o sistema iniciar
    """
    def tela_opcoes(self):
        print("----- Bem vindo à Biblioteca Gamer! -----")
        print("Selecione a opção desejada :")
        print("1: Usuários")
        print("2: Jogos")
        print("3: Aquisições")
        print("0: Sair")
        print("-----------------------------------------")
        opcao = self.verifica_opcao("Opção: ", [1,2,3,0])

        return opcao
    #  return [opcao, nome, genero, ano_lancamento, horas_jogadas, preco]
    # esse return esta devolvendo pro método abre_tela do contorlador do jogo. O controlador do usuario chama a tela e realiza o processo de leitura e impressao e retorna os valores. O controlador pega esses valores de retorno para realizar as operacoes
    # mas aí seria só retunr da opção e não todos esses outro atributos - André
    """