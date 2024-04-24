import json
import os

nome_arquivo = 'contatos.json'

class Opcoes:

    def __init__(self) -> None:
        pass
    
    def mensagem_encerrando(cls):
        os.system("cls")
        print("CRUD Encerrado")
            
    @classmethod
    def ListandoDados(cls, nome_arquivo='contatos.json'):
        try:
            with open(nome_arquivo, 'r') as file:
                dados = json.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado")
            return
        
        if not dados:
            print("Lista de contatos vazia")
            return
        
        for contato in dados:
            print(f'ID - {contato['id']}, Nome - {contato['nome']}, Número - {contato['numero']}, Idade - {contato['idade']}')
            

    def EditandoContato(self):
        try:
            with open(nome_arquivo, 'r') as file:
                dados = json.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado")
            return
        
        if not dados:
            print("Lista de contatos vazia")
            return
        
        for contato in dados:
            print(f'ID - {contato['id']}, Nome - {contato['nome']}, Número - {contato['numero']}, Idade - {contato['idade']}')
        
        id = input("Qual ID do contato que você deseja editar: ")