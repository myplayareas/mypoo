from models import Endereco, Pessoa, Usuario, Cliente
from utils import Validador
import os

try: 
    if os.name == 'posix':
        os.system("clear")
    # instancia Endereco
    endereco1 = Endereco(rua='Coelho de Resende', numero='222', cep=Validador.valida_cep('64000-0000'), cidade='Teresina', estado='PI')

    # instancia Pessoa
    pessoa1 = Pessoa(nome='Maria Joaquina de Amaral Pereira Goes', data_nascimento=Validador.valida_data('19/02/1980'), 
    sexo='M', cpf='123456789-87', telefone=Validador.valida_telefone('(86)995555558'), email=Validador.valida_email('teste@ufpi.edu.br'))

    # atribui enderedo1 a pessoa1
    pessoa1.set_endereco(endereco1)

    print(f'Nome: {pessoa1.nome}, Data de Nascimento: {pessoa1.data_nascimento}, Sexo: {pessoa1.sexo}, cpf: {pessoa1.cpf}, idade: { pessoa1.get_idade_atual() }, endereco: {pessoa1.endereco}')

    cliente1 = Cliente(pessoa1)

    cliente1.set_endereco(endereco1)

    print(cliente1.nome)

    usuario1 = Usuario('teste', 'teste', 1)

    cliente1.set_usuario(usuario1)

    print(f'Usuário do cliente1: {cliente1.usuario.user}')

except Exception as e:
    print(f'Erro: {e}')

