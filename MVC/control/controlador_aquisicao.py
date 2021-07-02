from MVC.view.tela_aquisicao import TelaAquisicao
from MVC.model.aquisicao import Aquisicao
from MVC.model.jogo import Jogo

class ControladorAquisicao:

    def __init__(self, controlador_biblioteca):
        self.__controlador_biblioteca = controlador_biblioteca
        self.__tela = TelaAquisicao(self)
        self.__aquisicoes = []


    def abre_tela(self):
      button, values =  self.__tela.open()
      if button == 'Comprar Jogo':
        print('entrou no loop')
        self.escolhe_jogo(values['opcao_jogo'], values['id_usuario'])
      elif button == 'Histórico de compras':
        self.listar_aquisicoes()
      else:
        self.__controlador_biblioteca.abre_tela()

     
    def escolhe_jogo(self, opcao_jogo: int, id_usuario: str):
      if opcao_jogo == '1':
        usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
        jogo_selecionado = "Age of empires 2"
        jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(jogo_selecionado)
        if float(jogo.preco) <= float(usuario.saldo) and jogo not in usuario.jogos_adquiridos:
              usuario.jogos_adquiridos.append(jogo)
              self.__aquisicoes.append(Aquisicao(usuario, jogo, "11/12/2020"))
              usuario.saldo = float(usuario.saldo) - float(jogo.preco)
              self.__tela.show_message("Aquisição", "Jogo adquirido com sucesso!")
        else:
            self.__tela.show_message("Usuário não possui saldo suficiente. Faltam R$"+ float(jogo.preco - usuario.saldo) + "  de saldo para a compra ser possível.")

      elif opcao_jogo == '2':
        usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
        jogo_selecionado = "Counter Strike GO"
        jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(jogo_selecionado)
        if float(jogo.preco) <= float(usuario.saldo) and jogo not in usuario.jogos_adquiridos:
              usuario.jogos_adquiridos.append(jogo)
              self.__aquisicoes.append(Aquisicao(usuario, jogo, "11/12/2020"))
              usuario.saldo = float(usuario.saldo) - float(jogo.preco)
              self.__tela.show_message("Aquisição", "Jogo adquirido com sucesso.")
        else:
            self.__tela.show_message("Usuário não possui saldo suficiente. Faltam R$"+ str(jogo.preco - usuario.saldo) + "  de saldo para a compra ser possível.")
      
      elif opcao_jogo == '3':
        usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
        jogo_selecionado = "Fifa 20"
        jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(jogo_selecionado)
        if float(jogo.preco) <= float(usuario.saldo) and jogo not in usuario.jogos_adquiridos:
              usuario.jogos_adquiridos.append(jogo)
              self.__aquisicoes.append(Aquisicao(usuario, jogo, "8/12/2020"))
              usuario.saldo = usuario.saldo - jogo.preco
              self.__tela.show_message("Aquisição", "Jogo adquirido com sucesso.")
        else:
            self.__tela.show_message("Usuário não possui saldo suficiente. Faltam R$"+ str(jogo.preco - usuario.saldo) + "  de saldo para a compra ser possível.")
      
      elif opcao_jogo == '4':
        usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
        jogo_selecionado = "Dota 2"
        jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(jogo_selecionado)
        if float(jogo.preco) <= float(usuario.saldo) and jogo not in usuario.jogos_adquiridos:
              usuario.jogos_adquiridos.append(jogo)
              self.__aquisicoes.append(Aquisicao(usuario, jogo, "8/12/2020"))
              usuario.saldo = float(usuario.saldo) - float(jogo.preco)
              self.__tela.show_message("Aquisição","Jogo adquirido com sucesso.")
        else:
            self.__tela.show_message("Usuário não possui saldo suficiente. Faltam R$"+ str(jogo.preco - usuario.saldo) + "  de saldo para a compra ser possível.")
      
      elif opcao_jogo == '5':
        usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
        jogo_selecionado = "Formula 1 2020"
        jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(jogo_selecionado)
        if float(jogo.preco) <= float(usuario.saldo) and jogo.nome not in usuario.jogos_adquiridos:
              usuario.jogos_adquiridos.append(jogo)
              self.__aquisicoes.append(Aquisicao(usuario, jogo, "8/12/2020"))
              usuario.saldo = float(usuario.saldo) - float(jogo.preco)
              self.__tela.show_message("Aquisição", "Jogo adquirido com sucesso.")
        else:
            self.__tela.show_message("Usuário não possui saldo suficiente. Faltam R$"+ str(jogo.preco - usuario.saldo) + "  de saldo para a compra ser possível.")
      elif opcao_jogo == 'Voltar ao menu principal':
        self.__controlador_jogo.abre_tela()
      
    def listar_aquisicoes(self):
        lista_aquisicoes = []
        for aquisicao in self.__aquisicoes:
          lista_aquisicoes.append(aquisicao.usuario.nome + " comprou " + aquisicao.jogo.nome + " no dia 11/12/2020" + "\n")
        self.__tela.show_message("Aquisições", lista_aquisicoes)


age2 = Jogo("Age of empires 2", "RTS", '1999', '0', '0', '50.00')
csgo = Jogo("Counter Strike GO", "FPS",'2012', '0', '0', '20.00')
fifa20 = Jogo("Fifa 20", "Esporte", '2019', '0', '0', '80.00' )
dota2 = Jogo("Dota 2", "MOBA", '2013', '0', '0', '15.00')
f12020 = Jogo("Formula 1 2020", "Corrida", '2020', '0', '0', '90.00')
     
   
   #def efetuar_aquisicao(self, id_usuario: str, jogo: Jogo)"
    # try:
     #   usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
     #   jogo = self.__controlador_biblioteca.controlador_jogo.escolhe_jogo()
     #except Exception:
     #   print("Usuário ou jogo não existente")
     #if (jogo.preco <= usuario.saldo): #falta verificar se o usuário já adquiriu o jogo antes
     #    usuario.saldo = usuario.saldo - jogo.preco
      #   self.__aquisicoes.append(Aquisicao(usuario, jogo, "11/05/2020"))
       #  print("Jogo adquirido!")
    # else:
        #  print("O usuário não tem saldo suficiente para adquirir este jogo.")""""
    
  
    

