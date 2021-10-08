import datetime

class Endereco:
    def __init__(self, rua, numero, complemento=None, cep=None, cidade=None, estado=None):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f'Rua: {self.rua} - n.o: {self.numero} - Cpl: {self.complemento} - CEP: {self.cep} - cidade: {self.cidade} - estado: {self.estado} '

class Pessoa:
    endereco = None
    def __init__(self, nome, data_nascimento, sexo, cpf, telefone=None, email=None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def get_idade_atual(self):
        ano_nascimento = self.data_nascimento.split('/')[2]
        data_corrente = datetime.datetime.now()
        ano_corrente = data_corrente.year
        return int(ano_corrente) - int(ano_nascimento)

    def set_endereco(self, endereco):
        self.endereco = endereco
    
    def __str__(self):
        return f'Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, Sexo: {self.sexo}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereco}'

class Usuario:
    def __init__(self, user, password, acesso=None):
        self.user = user
        self.password = password
        self.acesso = acesso

class Cliente(Pessoa):
    usuario = None

    def set_usuario(self, usuario):
        self.usuario = usuario

