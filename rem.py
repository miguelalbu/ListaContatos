import json
nome_arquivo = 'contatos.json'
class Rem:
    def __init__(self) -> None:
        pass

    @classmethod
    def RemovendoContato(cls):    
        try:
           with open(nome_arquivo, 'r', encoding='utf-8') as file:
                
                dados = json.load(file)

        except FileNotFoundError:
            print("Arquivo não encontrado")
            return

        if not dados:
            print("Lista de contatos está vazia")
            return

        nomes = []
        for contato in dados:
            nomes.append(contato['nome'])

        print("Contatos disponíveis:")
        print(", ".join(nomes))

        nome_del = input("Digite o nome do contato que deseja excluir: ").capitalize()
        indices = []
        for i, contato in enumerate(dados):
            if contato.get('nome') == nome_del:
                indices.append(i)

        if indices:
            for index in sorted(indices, reverse=True):
                del dados[index]
            
            
            with open(nome_arquivo, 'w', encoding='utf-8') as file:
                json.dump(dados, file, ensure_ascii=False, indent=4)

            
            print(f"Contato '{nome_del}' removido com sucesso.")
        else:
            print(f"Contato '{nome_del}' não encontrado.")