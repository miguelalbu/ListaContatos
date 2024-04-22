import json
import os
nome_arquivo = 'contatos.json'

class Add:
    def __init__(self) -> None:
        pass

    @classmethod
    def AdicionandoContato(cls, nome_arquivo=nome_arquivo):
        print("Adicionando contato...")
        while True:
            nome = input("Digite o nome do contato que deseja adicionar: ").capitalize() 
            with open(nome_arquivo, 'r') as file:
                dados = json.load(file)

            nome_existente = []

            for nomes in dados:
                nome_existente.append(nomes['nome'])
            
            if nome in nome_existente:
                print("Nome já existente na sua lista de contatos.")
                continue

            idade = int(input("Digite a idade da pessoa que você está adicionando: "))
            num = input("Digite o número do contato: ")
            
            if len(num) < 8:
                while len(num) < 8:
                    print("O número deve ter pelo menos 8 dígitos")
                    num = input("Digite o número NOVAMENTE: ")
            if len(num) >= 8:
                break
            

        try:
            with open(nome_arquivo, 'r') as file:
                dados = json.load(file)
        except FileNotFoundError:
            dados = []

        proximo_id = len(dados) + 1
        
        novo_contato = {
            'id': proximo_id,
            'nome': nome,
            'idade': idade,
            'numero': num
        }

        dados.append(novo_contato)
        
        with open(nome_arquivo, 'w') as file:
            json.dump(dados, file, indent=4)

        os.system("cls")
        print("\nContato cadastrado com sucesso!\n")