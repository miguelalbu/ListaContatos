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
            
    @classmethod
    def EditandoContato(cls):
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
            print(f"ID - {contato['id']}, Nome - {contato['nome']}, Número - {contato['numero']}, Idade - {contato['idade']}")
        
        id = input("Qual ID do contato que você deseja editar: ")

        for index, contato in enumerate(dados):
            if id == str(contato['id']): 
                print("ID Encontrado")
                alterando = int(input("O que você deseja alterar? (1 - Nome, 2 - Número): "))
                if alterando not in [1, 2]:
                    print("Opção inválida")
                elif alterando == 1:
                    nome_novo = input("Qual nome você deseja colocar: ")
                    dados[index]['nome'] = nome_novo
                    print("Nome alterado com sucesso!")
                elif alterando == 2:
                    num_novo = input("Qual número você deseja colocar: ")
                    dados[index]['numero'] = num_novo
                    print("Número alterado com sucesso!")
            else:
                os.system("cls")
                print("Contato não encontrado, TENTE NOVAMENTE")
                print()
                

        
        try:
            with open(nome_arquivo, 'w') as file:
                json.dump(dados, file)
        except Exception as e:
            print(f"Erro ao escrever no arquivo: {e}")
