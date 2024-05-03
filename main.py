import os
from rem import Rem
from options import Opcoes
from add import Add

opcoes = Opcoes()
add = Add()
rem = Rem()
while(True):
    op = int(input("Digite algum número abaixo para realizar uma ação\n1 - Adionar Contato\n2 - Remover Contato\n3 - Editar contato\n4 - Listar contatos\n0 - Encerrar Programa\n"))
    
    if(op > 4):
        os.system('cls')
        print("Opção INVÁLIDA, tente novamente")
        continue

    elif(op == 1):
        add.AdicionandoContato()

    elif(op == 2):
        rem.RemovendoContato()

    elif(op == 3):
        opcoes.EditandoContato()

    elif(op == 4):
        opcoes.ListandoDados()
        
    else:
        opcoes.mensagem_encerrando()
        break