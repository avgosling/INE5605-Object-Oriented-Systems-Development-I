from MVC.view.tela import Tela
import PySimpleGUI as sg


class TelaJogo(Tela):

    def __init__(self, controlador_jogo):
        self.__controlador_jogo = controlador_jogo
        self.__window_pesquisa = None
        self.__window_menu = None

    def init_components(self):
        sg.ChangeLookAndFeel('SandyBeach')
        layout_menu_jogo =     [
                                [sg.Text('JOGOS')],
                                [sg.Text('Clique em uma opção do menu abaixo:', size=(45, 1))],
                                [sg.Button('Listar Jogos')],
                                [sg.Button('Pesquisar Jogo')],
                                [sg.Button('Voltar ao menu Principal')]
                               ]
        
        layout_pesquisa_jogo = [
                                [sg.Text('Pesquisa de Jogos')],
                                [sg.InputText('Insira o nome do jogo', key='nome')],
                                [sg.Submit()]
                               ]

        self.__window_menu = sg.Window('Menu de Jogos').Layout(layout_menu_jogo)
        self.__window_pesquisa = sg.Window('Pesquisar Jogo').Layout(layout_pesquisa_jogo)

    def open(self):
        self.init_components()
        button, values = self.__window_menu.Read()
        if button == 'Pesquisar Jogo':
          button2, values = self.__window_pesquisa.Read()
        elif button == 'Voltar a menu principal':
            return button, values
        self.close()
        return button, values

    def close(self):
        self.__window_menu.Close()
        self.__window_pesquisa.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
