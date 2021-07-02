from MVC.control.controlador_biblioteca import ControladorBiblioteca

if __name__ == "__main__":
  #instancia o controlador principal do sistema e chama o metodo que abre a tela inicial desse sistema
  controlador_biblioteca = ControladorBiblioteca()
  controlador_biblioteca.abre_tela()