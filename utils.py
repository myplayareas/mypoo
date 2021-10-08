import datetime
import re

class Validador:
    padrao_telefone_com_ddd = "[(][0-9]{2}[)][0-9]{4,5}[-]*[0-9]{4}"
    padrao_email = "[a-zA-Z0-9_.]{1,30}@[a-zA-Z0-9_.]{1,30}"
    padrao_data_nascimento = '[0-9]{2}[/][0-9]{2}[/][0-9]{4}'
    padrao_cep = '[0-9]{5}[-][0-9]{3}'

    @classmethod
    def valida_telefone(cls,telefone):
        checa_telefone = re.match(cls.padrao_telefone_com_ddd, telefone)
        if checa_telefone is not None:
            return telefone
        else:
            mensagem = f'Telefone {telefone} inválido! A formatação deve ser (XX)XXXXX-XXXX ou (XX)XXXX-XXXX'
            raise Exception(mensagem)

    @classmethod
    def valida_email(cls, email):
        checa_email = re.match(cls.padrao_email, email)
        if checa_email is not None:
            return email
        else:
            mensagem = f'E-mail {email} inválido! A formatação deve ser xxxx@yyyy.zzz...'
            raise Exception(mensagem)

    @classmethod
    def valida_data(cls, data): 
        checa_data = re.match(cls.padrao_data_nascimento, data)
        if checa_data is not None : 
            dia = data.split('/')[0]
            mes = data.split('/')[1]
            ano = data.split('/')[2]
            try:
                data_auxiliar = datetime.datetime(int(ano), int(mes), int(dia) )
            except Exception as e:
                print(f'Data {data} inválida! {e}')    
            return data
        else:
            mensagem = f'Data {data} inválida! A formatação deve ser dd/mm/yyyy'
            raise Exception(mensagem)

    @classmethod
    def valida_cep(cls, cep):
        checa_cep = re.match(cls.padrao_cep, cep)
        if checa_cep is not None:
            return cep
        else:
            mensagem = f'CEP {cep} inválido! A formatação deve ser XXXXX-XXX'
            raise Exception(mensagem)