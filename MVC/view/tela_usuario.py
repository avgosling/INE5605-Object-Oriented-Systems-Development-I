from MVC.view.tela import Tela
import PySimpleGUI as sg


class TelaUsuario(Tela):
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__controlador_usuario = controlador
        self.__window_cadastro = None
        self.__window_menu = None
        self.__window_exclusao = None
        self.__window_pesquisa_id = None
        self.__window_adicao_saldo = None
        self.__window_alterar_email = None
        self.__hide = False

    # esse método recebe uma lista como parametro, percorre ela e exibe os elementos da mesma
    def init_components(self):
      sg.ChangeLookAndFeel('SandyBeach')
      layout_cadastro_usuario = [
                                    [sg.Text('Cadastro de um novo usuário')],
                                    [sg.InputText('Qual o nome do usuario?', key='nome')],
                                    [sg.InputText('Qual o email do usuario?', key='email')],
                                    [sg.InputText('Qual id do usuário?', key='id_usuario')],
                                    [sg.InputText('Saldo inicial', key='saldo')],
                                    [sg.Submit()]
                                ]

      layout_menu_usuario =     [
                                    
                                    [sg.Text('Escolha uma opção do menu abaixo')],
                                    [sg.Button('Criar usuário')],
                                    [sg.Button('Remover usuário')],
                                    [sg.Button('Usuários existentes')],
                                    [sg.Button('Pesquisar por ID')],
                                    [sg.Button('Adicionar saldo')],
                                    [sg.Button('Alterar email')],
                                    [sg.Button('Voltar ao menu principal')]
                                ]

      layout_exclusao_usuario = [
                                    [sg.Text('Exclusão de um usuário')],
                                    [sg.InputText('Digite o ID do usuário', key='id_usuario')],
                                    [sg.Submit()]
                                ]
      
      layout_pesquisa_por_id =  [
                                    [sg.InputText('Digite o id do usuário que deseja pesquisar', key='id_usuario')],
                                    [sg.Submit()]
                                ]
      layout_adicao_saldo =    [
                                    [sg.InputText('Senha de administrador', key='password')],
                                    [sg.InputText(('Digite o ID do Usuário'), key ='id_usuario')],
                                    [sg.InputText('Digite o valor que deseja adicionar no saldo', key='saldo')],
                                    [sg.Submit()]
                               ]
      layout_alteracao_email = [
                                    [sg.InputText('Qual id do usuário?', key='id_usuario')],
                                    [sg.InputText('Qual o novo e-mail?', key = 'email')],
                                    [sg.Submit()]
                               ]
      self.__window_cadastro = sg.Window('Cadastro de Usuários').Layout(layout_cadastro_usuario)
      self.__window_exclusao = sg.Window('Remoção de Usuários').Layout(layout_exclusao_usuario)
      self.__window_menu = sg.Window('Menu de Usuários').Layout(layout_menu_usuario)
      self.__window_pesquisa_id = sg.Window('Pesquisa de Usuários por ID').Layout(layout_pesquisa_por_id)
      self.__window_adicao_saldo = sg.Window('Adição de Saldo').Layout(layout_adicao_saldo)
      self.__window_alterar_email = sg.Window('Alteração de E-mail').Layout(layout_alteracao_email)

    def open_menu(self):
      self.init_components()
      button, values = self.__window_menu.Read()
      if button == 'Criar usuário':
        button2, values = self.__window_cadastro.Read()
        self.close()
      elif button == 'Remover usuário':
        button2, values = self.__window_exclusao.Read()
        self.close()
      elif button == 'Pesquisar por ID':
        button2, values = self.__window_pesquisa_id.Read()
        self.close()
      elif button == 'Adicionar saldo':
        button2, values = self.__window_adicao_saldo.Read()
        self.close()
      elif button == 'Alterar email':
        button2, values = self.__window_alterar_email.Read()
        self.close()
      return button, values
        
    def close(self):
        self.__window_menu.Close()
        self.__window_cadastro.Close()
        self.__window_adicao_saldo.Close()
        self.__window_alterar_email.Close()
        self.__window_pesquisa_id.Close()
        self.__window_exclusao.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def exibir_menu_opcoes(self, lista: []):
        for elem in lista:
            print(elem)

    def verifica_opcao(self, msg: str = "", opcoes_validas: [] = None):
        while True:
            valor_lido = input(msg)
            try:
                inteiro = int(valor_lido)
                if opcoes_validas and inteiro not in opcoes_validas:
                    raise ValueError
                return inteiro
            except ValueError:
                sg.Popup("Erro", "Digite uma opção válida.")
    
    def tratar_float_str(self, msg=""):
      while True:
        try:
          resposta = float(input(msg))
          return resposta
        except ValueError:
          sg.Popup("Erro", "Resposta inválida. Verifique se está usando apenas números e se está usando ponto(exemplo 100.00).")

    def tratar_int_str(self, msg=""):
        while True:
            try:
                resposta = int(input(msg))
                return resposta
            except ValueError:
                sg.Popup("Erro", "Resposta inválida. Verifique se está usando apenas números.")
    """
    def tela_opcoes(self):
        print("----- USUÁRIOS -----")
        print("Escolha uma opção do menu abaixo:")
        print("1: Criar usuário")
        print("2: Remover usuário")
        print("3: Usuários existentes")
        print("4: Pesquisar por ID")
        print("5: Adicionar saldo")
        print("6: Alterar email")
        print("0: Voltar ao menu principal")
        print("--------------------")
        opcao = self.verifica_opcao("Opção: ", [1,2,3,4,5,6,0])
    
        # # tratar quando o usuário não digitar nem 1,2,3 e opção 0 para voltar para o menu principal
        # a variável inicia vazia e só recebe um valor de fato se as opcoes selecionadas forem 1 ou 2
        # e o método listar usuário por ID? falta incluir ali - André
        #nome = None
        if opcao == 1:
            nome = input("Qual o nome do usuario? : ")
            email = input("Qual o email do usuario? : ")
            id_usuario = self.tratar_int_str("Qual id do usuário? : ")
            saldo = self.tratar_float_str("Saldo inicial: ")
            senha = None
            return [opcao, nome, email, id_usuario, saldo, senha]

        elif opcao == 2:
            nome = None
            email = None
            id_usuario = self.tratar_int_str("Digite o id do usuário que deseja remover: ")
            saldo = None
            senha = None
            return [opcao, nome, email, id_usuario, saldo, senha]
        elif opcao == 3:
            nome = None
            email = None
            id_usuario = None
            saldo = None
            senha = None
            return [opcao, nome, email, id_usuario, saldo, senha]
        elif opcao == 4:
            nome = None
            email = None
            id_usuario = self.tratar_int_str("Digite o id do usuário que deseja pesquisar: ")
            saldo = None
            senha = None
            return [opcao, nome, email, id_usuario, saldo, senha]
        elif opcao == 5:
            nome = None
            email = None
            senha = input("Para essa operação é necessária a senha de administrador. Digite :")
            id_usuario = self.tratar_int_str("Qual id do usuário? : ")
            saldo = self.tratar_float_str("Adicionar quanto? : ")
            return [opcao, nome, email, id_usuario, saldo, senha]
        elif opcao == 6:
            nome = None
            id_usuario = self.tratar_int_str("Qual id do usuário? : ")
            email = input("Qual será o novo email? : ")
            saldo = None
            senha = None
            return [opcao, nome, email, id_usuario, saldo, senha]

        elif opcao == 0:
            nome = None
            email = None
            id_usuario = None
            saldo = None
            senha = None
            return [opcao, nome, email, id_usuario, saldo, senha]
    """
    def mostra_msg_de_erro(self, msg: str):
        sg.Popup(msg)
 # esse return esta devolvendo pro método abre_tela do contorlador do usuario. O controlador do usuario chama a tela e realiza o processo de leitura e impressao e retorna os valores. O controlador pega esses valores de retorno para realizar alguma operacao