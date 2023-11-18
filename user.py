class User:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

def criar_usuario():
    # Obter os valores dos campos de entrada
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")
    # Criar uma instância de User
    novo_usuario = User(email, senha)

# Chamar a função criar_usuario para criar um novo usuário
criar_usuario()