from MVC.model.usuario import Usuario
from MVC.model.jogo import Jogo

class Aquisicao:
  def __init__ (self, usuario: Usuario, jogo: Jogo, data_aquisicao:str,):
    self.__usuario = usuario
    self.__jogo = jogo
    self.__data_aquisicao = data_aquisicao

  
  @property
  def data_aquisicao(self):
    return self.__data_aquisicao
  
  @data_aquisicao.setter
  def data_aquisicao(self, data_aquisicao: str):
    if isinstance(data_aquisicao,str):
      self.__data_aquisicao = data_aquisicao

   
  @property
  def usuario(self):
    return self.__usuario

  @usuario.setter
  def usuario(self, usuario):
    if isinstance(usuario, Usuario):
      self.__usuario = usuario

  @property
  def jogo(self):
    return self.__jogo

  @jogo.setter
  def jogo(self, jogo):
    if isinstance(jogo, Jogo):
      self.__jogo = jogo