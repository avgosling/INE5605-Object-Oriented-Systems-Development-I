from MVC.view.tela_biblioteca import TelaBiblioteca
from MVC.control.controlador_jogo import ControladorJogo
from MVC.control.controlador_usuario import ControladorUsuario
from MVC.control.controlador_aquisicao import ControladorAquisicao

class ControladorBiblioteca:
  def __init__(self):

    self.__tela = TelaBiblioteca(self)
    self.__controlador_usuario = ControladorUsuario(self)
    self.__controlador_jogo = ControladorJogo(self)
    self.__controlador_aquisicao = ControladorAquisicao(self)
    self.__senha_admin = "ok11blz"


  def abre_tela(self):
    while True: 
      button, values = self.__tela.open()
      if button == 'Usuários':
        self.__controlador_usuario.abre_tela()
      
      elif button == 'Jogos':
        self.__controlador_jogo.abre_tela()
      
      elif button == 'Aquisições':
        self.__controlador_aquisicao.abre_tela()

      elif button == 'Sair':
        self.__tela.show_message("Adeus", "Até breve!")
        break
      
  
  @property
  def controlador_usuario(self):
    return self.__controlador_usuario
  
  @property
  def controlador_jogo(self):
    return self.__controlador_jogo
  
  @property
  def controlador_aquisicao(self):
    return self.__controlador_aquisicao