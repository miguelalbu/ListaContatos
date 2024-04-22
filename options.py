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
    def ListandoDados(cls, nome_arquivo = nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as file:
                dados = json.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado")
            return
        
        if not dados:
            print("Lista de contatos vazia")
            return
        
        nomes = []

        for contato in dados:
            nomes.append(contato['nome'])
        
        os.system('cls')
        print("Listando contatos...")
        print(", ".join(nomes))
        print()
        

    def EditandoContato(self):
        pass
        