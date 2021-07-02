from MVC.model.dao import DAO
from MVC.model.usuario import Usuario

class UsuarioDAO(DAO):
  def __init__(self):
    super().__init__('usuarios.pkl')
  
  def add(self, usuario: Usuario):
    if usuario is not  None and  isinstance(usuario, Usuario) and isinstance(usuario.nome, str):
      super().add(usuario.nome, usuario)


  def get(self, key: str):
    if isinstance(key, str):
      return super().get(key)
  
  def remove(self, key: str):
    if isinstance(key, str):
      super().remove(key)