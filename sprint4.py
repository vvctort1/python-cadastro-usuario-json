from modulo_matriz import loginEmpresa,loginCliente,atualizarListaClientes
import json


# TRY EXCEPT COMENTADOS PARA VERIFICAR ERROS

# COLOCAR CORES E EDITAR VIZUALIZAÇÃO NO TERMINAL

# IMPLEMENTAR ALGUMA API, TALVEZ NO CADASTRO DE USUÁRIO

# COMENTAR CÓDIGO

# DESCRIÇÃO DO PROJETO NO ARQUIVO integrantes.txt

lista_de_clientes = []

with open("clientes.json","r") as arquivo:
    lista = json.load(arquivo)

for item in lista:
    lista_de_clientes.append(item)

while True:


    # try:
        print("""\033[1;33m
    --------------------------------
    Seja bem vindo(a)!

    0 - Sair;

    1 - Sou Cliente;

    2 - Sou Empresa.
    --------------------------------
    \033[m""")

        escolha = int(input("Escolha uma das opções de login: "))

        if escolha == 0:
            print("Encerrando o programa...")
            print("Obrigado por utilizar nosso programa! Programa encerrado com sucesso.")
            break
        elif escolha == 1:
            loginCliente(atualizarListaClientes())
        elif escolha == 2:
            loginEmpresa(lista_de_clientes)
        else: 
            print("\n\033[1;31mDigite 0, 1 ou 2!\033[m")
    # except ValueError:
    #     print("\n\033[1;31mValor inválido! Tente novamente...\033[m")
    # except Exception:
    #     print("\n\033[1;31mOcorreu um erro inesperado! Tente novamente...\033[m")
