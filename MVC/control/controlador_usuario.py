from MVC.model.usuario import Usuario
from MVC.view.tela_usuario import TelaUsuario
from MVC.model.usuarioDAO import UsuarioDAO

class ControladorUsuario:
  def __init__(self, controlador_biblioteca):
      self.__controlador_biblioteca = controlador_biblioteca
      self.__tela = TelaUsuario(self)
      self.__usuarios = UsuarioDAO()
      self.__senha_admin = "ok11blz"

  def abre_tela(self):
    button, values =  self.__tela.open_menu()
    if button == 'Criar usuário':
      self.incluir_usuario(values['nome'],values['email'], values['id_usuario'],values['saldo'],[]) 
    elif button == 'Remover usuário':
      self.excluir_usuario(values['id_usuario'])
    elif button == 'Usuários existentes': 
      self.listar_usuarios()
    elif button == 'Pesquisar por ID':
      self.pesquisar_usuario(values['id_usuario'])
    elif button == 'Adicionar saldo':
      self.adicionar_saldo(values['id_usuario'], float(values['saldo']), values['password'])
    elif button == 'Alterar email':
      self.altera_email(values['id_usuario'],values['email'])
    elif button == 'Voltar ao menu principal':
      self.__controlador_biblioteca.abre_tela()


  def incluir_usuario(self, nome: str, email: str, id_usuario: str, saldo: float, jogos_adquiridos):
    try:
      for usuario in self.__usuarios.get_all():
        if usuario.id_usuario == id_usuario:
          raise Exception()
    except Exception:
      self.__tela.show_message("Usuários", "Usuário já existente no sistema")
    else:
      self.__usuarios.add(Usuario(nome,email,id_usuario,saldo,jogos_adquiridos))
      self.__tela.show_message("Usuários", "Usuário adicionado com sucesso.")

  def excluir_usuario(self, id_usuario: str):
    try:
          self.__usuarios.remove(id_usuario)
    except KeyError:
      self.__tela.show_message("Usuários", "Erro na exclusao.") 
    
  def listar_usuarios(self):
    lista_usuarios = ''
    for usuario in self.__usuarios.get_all():
      lista_usuarios += "Nome: " + usuario.nome + '\n' + "Email: " + usuario.email + '\n' + "ID: " + usuario.id_usuario + '\n' + '\n'
    self.__tela.show_message('Usuários', lista_usuarios)

  def listar_usuario_por_id(self, id_usuario: str):
    for usuario in self.__usuarios.get_all():
      if usuario.id_usuario == id_usuario:
        self.__tela.show_message("Usuários", usuario.nome + "  encontrado")
      return usuario


  def pesquisar_usuario(self, id_usuario: str):
    try:
      usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
    except Exception:
      self.__tela.show_message("Erro de Pesquisa", "Usuário não encontrado.")
    else:      
          self.__tela.show_message("Usuários",usuario.nome +  "\nID: " + str(usuario.id_usuario)  + "\nSaldo: R$" + str(usuario.saldo) + "\nJogos: " + str(self.listar_jogos_adquiridos(id_usuario)) + '\n') 
   
      

  
  def adicionar_saldo(self, id_usuario: str, saldo: float, senha: str):
    self.__senha_admin = "ok11blz"
    try:
      if senha != self.__senha_admin:
        raise Exception()
    except Exception:
        self.__tela.show_message("Erro de senha", "Senha incorreta.") 
    else:
      try:
        usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
      except Exception:
        self.__tela.show_message("Usuário não encontrado")
      else:
        usuario.saldo = float(usuario.saldo) + float(saldo)
        self.__tela.show_message("Saldo", "Saldo adicionado com sucesso")
       
  
  def altera_email(self, id_usuario: str, email: str):
    try:
        usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
    except Exception:
        self.__tela.show_message("Usuário não encontrado")
    else:
      usuario.email = email
      self.__tela.show_message("Email do usuário " , usuario.nome + " alterado.")
      
  def listar_jogos_adquiridos(self, id_usuario: str):
    try:
     usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
    except Exception:
      print('')
    else:
      for jogo in usuario.jogos_adquiridos:
        return jogo.nome + " - "

    
    
   