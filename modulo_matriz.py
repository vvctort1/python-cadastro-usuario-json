from random import randint
import json


# ///////////////// PARTE DO LOGIN DA EMPRESA /////////////////////////////////////////////////////////////

def loginEmpresa(clientes: list) -> None:
    """
    Função que mostra um menu com opções para o usuário, simulando o uso da ferramenta por um funcionário da empresa.
    """
    while True:
        try:
            print("""\033[1;33m
    ----------------------------
          Login Empresa

    0 - Sair;

    1 - Efetuar novo cadastro;

    2 - Buscar cliente existente;

    3 - Verificar estado de algum veículo cadastrado;

    4 - Consultar tokens de clientes.
            \033[m""")


            escolha = int(input("Escolha uma das opções acima: "))

            if escolha == 0:
                print("\033[1;32mLogout feito!\033[m")
                break
            elif escolha == 1:
                print("Abrindo nova ficha cadastral...")
                cadastroCliente(clientes)
            elif escolha == 2:
                dadosClientes()
            elif escolha == 3:
                situacaoVeiculo()
            elif escolha == 4:
                verificarToken()
            else:
                print("\n\033[1;31mDigite 0, 1, 2, 3 ou 4 apenas!\033[m")
        except ValueError:
            print("\n\033[1;31mValor inválido! Tente novamente...\033[m")
        except Exception:
            print("\n\033[1;31mOcorreu um erro inesperado!\033[m")



def cadastroCliente(clientes: list) -> None:
    """
    Função que gera um número aleatório utilizando a biblioteca random, definindo-o como chave do dicionário principal. Pede para que o usuário digite seus dados e armazena no valor do dicionário principal no formato de outro dicionário. Printando sucesso na tela assim que todos os dados tiverem sido preenchidos corretamente na ficha de cadastro. Após, pega o dicionário criado transformado-o em um json, armazenado num arquivo json.
    """
    while True:
        try:
            dicionario = {}

            token = randint(1000,100000)
            credito = randint(500,3000)
            print("\033[3;34mFicha Cadastral\033[m")
            print("\033[4;34mDados do(a) Cliente\n\033[m")

            nome = input("Nome: ").upper().strip()
            idade = int(input("Idade: "))
            carro = input("Veículo adquirido: ").upper().strip()
            placa = input("Placa do veículo: ").upper().strip()
            dicionario[token] = {nome: {"idade":idade,"carro":carro,"placa":placa,"credito":credito}}
            clientes.append(dicionario)


            with open("clientes.json","w",encoding="utf-8") as arquivo:
                json.dump(clientes,arquivo,indent=4,ensure_ascii=False)

                print("\n\033[1;32mCadastro efetuado!\033[m")
                break
        except ValueError:
            print("Valor inválido! Tente novamente...")
        except Exception:
            print("Ocorreu um erro inesperado! Tente novamente...")
   


def dadosClientes() -> None:
    """
    Função que pede o nome do(a) cliente para efetuar uma busca, verificando os dados e printando na tela, caso a pessoa esteja cadastrada. Também aparece a quantidade de pessoas encontradas com o nome digitado.
    """
    cont = 0
    nome = input("\nDigite o nome do(a) cliente: ").upper().strip()   

    with open("clientes.json","r") as arquivo:

        lista = json.load(arquivo)

        for clientes in lista:
            for cliente in clientes.values():
                for nome_cliente, dados in cliente.items():
                    if nome == nome_cliente:
                        cont += 1
                        print(f"\n\033[1;34mCliente encontrado: {nome} tem {dados['idade']} anos de idade e adquiriu o veículo {dados['carro']} placa {dados['placa']} nesta concessionária.\033    [m")
    print(f"\n\033[1;37m{cont} resultado(s) de pesquisa.\033[m")
                    


def situacaoVeiculo() -> None:
    """
    Função que pede ao usuário para digitar a placa de um veículo, se a placa estiver cadastrada, exibirá o nome do veículo e do proprietário. Caso não haja cadastro, apenas irá exibir que a placa não possui cadastro.
    """
    cont = 0
    placa = input("\nDigite a placa do veículo: ").upper().strip()

    with open("clientes.json","r") as arquivo:

        lista = json.load(arquivo)

        for clientes in lista:
            for cliente in clientes.values():
                for nome_cliente,dados in cliente.items():
                    if placa == dados['placa']:
                        cont += 1
                        quantidade_adequada_gases = randint(110, 121)
                        gases_expelidos = randint(110,121)

                        if gases_expelidos < quantidade_adequada_gases:
                            print(f"""\033[1;34m
Placa {placa} encontrada! O(A) proprietário(a) é o(a) Sr(a).{nome_cliente} e o veículo é um {dados['carro']}.

Para o veículo {dados['carro']}:

Quantidade máxima adequada de gases expelidos: {quantidade_adequada_gases}gCO2/km.

Quantidade média expelida pelo veículo {dados['carro']} pertencente a(o) Sr(a).{nome_cliente}: {gases_expelidos}gCO2/km.
                            
\033[1;32mO veículo está com a média de gases expelidos dentro do esperado, não é necessário fazer revisão.\033[m
\033[m
""")
                        elif gases_expelidos >= quantidade_adequada_gases:
                            print(f"""\033[1;34m
Placa {placa} encontrada! O(A) proprietário(a) é o(a) Sr(a).{nome_cliente} e o veículo é um {dados['carro']}.

Para o veículo {dados['carro']}:

Quantidade máxima adequada de gases expelidos: {quantidade_adequada_gases}gCO2/km.

Quantidade média expelida pelo veículo {dados['carro']} pertencente a(o) Sr(a).{nome_cliente}: {gases_expelidos}gCO2/km.
                            
\033[1;31mO veículo está expelindo quantidades de gases acima do esperado, é necessário fazer revisão.\033[m
\033[m
""")
    print(f"\033[1;37m{cont} resultado(s) de pesquisa.\033[m")



def verificarToken() -> None:
    """
    Função que pede ao usuário digitar o nome do cliente que deseja consultar o token. Abre o arquivo json e verifica se há algum cliente cadastrado com o mesmo nome digitado pelo usuário, printando o token em caso positivo.
    """
    cont = 0
    nome = input("\nDigite o nome do cliente: ").upper().strip()

    with open("clientes.json","r") as arquivo: 

        lista = json.load(arquivo)

        for clientes in lista:
          for token, cliente in clientes.items():
              for nome_cliente in cliente.keys():
                if nome == nome_cliente:
                    cont += 1
                    print(f"\n\033[1;34mO token do cliente {nome} : {token}\033[m")
        print(f"\n\033[1;37m{cont} resultado(s) de pesquisa\033[m")



# ///////////////// PARTE DO LOGIN DO CLIENTE /////////////////////////////////////////////////////////////

def loginCliente(clientes: list) -> None:
    """
    Função que printa uma menu com 2 opções para o usuário.
    """
    while True:
        try:
            print("""\033[1;33m
---------------------------------
            \nLogin Cliente
                  
0 - Voltar para o Menu Principal
            
1 - Efetuar Login de Cliente
                  
---------------------------------
\033[m""")
            escolha = int(input("\nDigite sua escolha: "))
            if escolha == 0:
                print("\033[1;32mVoltando para o Menu Principal...\033[m")
                break
            elif escolha == 1:
                token = input("\nDigite seu token (é necessário ter cadastro pela empresa): ")

                for cliente in clientes:
                    for token_cliente in cliente.keys():
                        if token == token_cliente:
                            print("\n\033[1;32mDirecionando para a área do  cliente...\033[m")
                            areaCliente(cliente,clientes,token)
                            break

                if token != token_cliente:
                    print("\n\033[1;31mToken não cadastrado! Verifique se digitou corretamente...\033[m")
            else:
                print("Escolha 0 ou 1 para a escolha ser válida!")
        except ValueError:
            print("\n\033[1;31mValor inválido! Tente novamente...\033[m")
        except Exception:
            print("\n\033[1;31mOcorreu um erro inesperado! Tente novamente...\033[m")
    


def areaCliente(cliente: dict,clientes: list,token: str) -> None:
    """
    Função que apresenta um menu com opções para o usuário. Simulando o uso do app por um cliente cadastrado.
    """
    while True:
        try:
            for nome in cliente[token].keys():
                print(f'''\033[1;33m
--------------------------------
Seja Bem Vindo(a) Sr(a). {nome}!

0 - Logout;

1 - Verificar dados;

2 - Status do carro;

3 - Verificar quantidade de crédito;

4 - Loja;

5 - Editar cadastro;

6 - Excluir cadastro.
--------------------------------
\033[m''')
            escolha = int(input("\nDigite sua escolha: "))

            if escolha == 0:
                print("\n\033[1;32mFazendo logout...\033[m")
                break
            elif escolha == 1:
                dadosCliente(cliente,token)
            elif escolha == 2:
                statusVeiculo(cliente,token)
            elif escolha == 3:
                quantidadeCredito(cliente,token)
            elif escolha == 4:
                lojaCliente()
            elif escolha == 5:
                editarDados(cliente,clientes)
            elif escolha == 6:
                excluirCadastro(cliente,clientes)
                break
            else:
                print("\n\033[1;31mDigite 0, 1, 2, 3, 4, 5 ou 6!\033[m")
        except ValueError:
            print("\n\033[1;31mDigite valores válidos\033[m")
        except Exception:
            print("\n\033[1;31mOcorreu um erro inesperado!\033[m")



def dadosCliente(cliente: dict,token: str) -> None:
    """
    Função que mostra ao usuário algumas informações referentes ao cliente logado.
    """
    
    for nome,dados in cliente[token].items():
                print(f"""\033[1;34m
Dados do(a) Cliente {nome}

Idade : {dados['idade']};
Carro : {dados['carro']};
Placa : {dados['placa']}.
\033[m""")



def statusVeiculo(cliente: dict,token: str) -> None:
    """
    Função que mostra ao cliente a quantidade de gases expelidos por seu carro alertando-o se é necessário ou não levar seu veículo para fazer manutenção.
    """
 
    for nome,dados in cliente[token].items():
        quantidadeAdequadaGases = randint(110, 121)   # Gera um número aleatório para simular a média esperada de gases expelidos pelveículo.
        gasesExpelidos = randint(110, 121)    # Gera um número aleatório para simular a quantidade de gases expelidos pelo veículo.
        if gasesExpelidos < quantidadeAdequadaGases:  # Se a quantidade de gases expelidos for menor que a média.
            print(f"""\033[1;34m
O(A) proprietário(a) Sr(a).{nome} possui o veículo {dados['carro']} placa {dados['placa']}.

Para o veículo {dados['carro']}:

Quantidade máxima adequada de gases expelidos: {quantidadeAdequadaGases}gCO2/km.

Quantidade média expelida pelo veículo {dados['carro']} pertencente a(o) Sr(a).{nome}: {gasesExpelidos}gCO2/km.
                            
\033[1;32mO veículo está com a média de gases expelidos dentro do esperado, não é necessário fazer revisão.\033[m
\033[m""")  
        elif gasesExpelidos > quantidadeAdequadaGases:  #  Se a quantidade de gases expelidos forem maiores ou igual a média.
            print(f"""\033[1;34m
O(A) proprietário(a) Sr(a).{nome} possui o veículo {dados['carro']} placa {dados['placa']}.

Para o veículo {dados['carro']}:

Quantidade máxima adequada de gases expelidos: {quantidadeAdequadaGases}gCO2/km.

Quantidade média expelida pelo veículo {dados['carro']} pertencente a(o) Sr(a).{nome}: {gasesExpelidos}gCO2/km.
                            
\033[1;31mO veículo está expelindo quantidades de gases acima do esperado, é necessário fazer revisão.\033[m
\033[m""")



def quantidadeCredito(cliente: dict,token: str) -> None:
    """
    Função que printa no terminal a quantidade de créditos que o cliente logado possui disponível.
    """
    for nome,dados in cliente[token].items():
        print(f"\n\033[1;34m{nome} acumulou {dados['credito']} créditos por manter seu veículo em ordem. Obrigado por contribuir com o meio ambiente e ajudar a tornar o mundo num lugar mais limpo!\033[m")



def lojaCliente() -> None:
    """
    Função que apresenta ao usuário uma loja de produtos e serviços para veículos.
    """
    print("""
Revisão Gratuita para o seu veículo  -  500 créditos

Som Pioneer  -  1200 créditos
          
Bagageiro de Teto  -  1200 créditos
          
Desconto de 5% na compra de um novo veículo  -  2500 créditos
          
Pintura  -  1500 créditos

Park Assist  -  1000 créditos
        
Lavagem Completa  -  100 créditos
          
(Obs: Para trocar seus créditos por algum dos serviços disponibilizados vá até alguma de nossas empresas parceiras.)
""")
    


def excluirCadastro(cliente: dict,clientes: list) -> None:
    """
    Função que mostra um pequeno menu para o usuário com a opção de cancelar a exclusão do cadastro ou prosseguir, caso o usuário decida prosseguir, o cliente é excluído do arquivo json e o usuário é direcionado para o Menu para logar o cliente. Não sendo mais possível logar utilizando o token excluído.
    """
    while True:
        try:
            print("""\033[1;33m

Você tem certeza que deseja excluir seu cadastro?
                              
0 - Cancelar;
                              
1 - Prosseguir.

\033[m""")
            escolha = int(input('\nDigite sua escolha: '))

            if escolha == 0:
                break
            elif escolha == 1:

                clientes.remove(cliente)

                for nome in cliente.keys():
                    print(f"\033[1;32mO cadastro do cliente {nome} foi removido com sucesso!\033[m")

                with open("clientes.json","w",encoding="utf-8") as arquivo:
                    json.dump(clientes,arquivo,indent=4)

                break
            else:
                print("\033[1;31mEscolha 0 ou 1 para a escolha ser válida!\033[m")
        except ValueError:
            print("\033[1;31mDigite valores válidos!\033[m")
        except Exception:
            print("\033[1;31mOcorreu um erro inesperado!\033[m")



def editarDados(cliente: dict, clientes: list) -> None:
    """
    Função que mostra um menu de opções para o usuário escolher o dado cadastrado que deseja editar. Fazendo as respectivas atualizações de edição no arquivo json e no programa.
    """
    while True:
        try:
            print("""\033[1;33m

O que você deseja editar?
                              
0 - Sair da edição;
                              
1 - Sua idade;
                              
2 - O modelo do seu veículo;
                              
3 - A placa do seu veículo;
                              
4 - Editar todos os dados.

\033[m""")
            escolha = int(input("\nDigite sua escolha: "))

            if escolha == 0:
                break
            elif escolha == 1:
                print("\n\033[1;34mEditando Idade\033[m\n")
                novo_idade = int(input("Digite sua idade: "))

                for dados in cliente.values():
                    for dado in dados.values():
                        dado["idade"] = novo_idade
                        dado["carro"] = dado["carro"]
                        dado["placa"] = dado["placa"]
                        dado["credito"] = dado["credito"]

                with open("clientes.json","w",encoding="utf-8") as arquivo:
                    json.dump(clientes,arquivo,indent=4)

                print("\033[1;32mIdade editada com sucesso!\033[m")

            elif escolha == 2:
                print("\n\033[1;34mEditando Modelo do Veículo\033[m\n")
                novo_carro = input("Digite o nome do modelo: ").upper().strip()

                for dados in cliente.values():
                    for dado in dados.values():
                        dado["idade"] = dado["idade"]
                        dado["carro"] = novo_carro
                        dado["placa"] = dado["placa"]
                        dado["credito"] = dado["credito"]

                with open("clientes.json","w",encoding="utf-8") as arquivo:
                    json.dump(clientes,arquivo,indent=4)
                
                print("\033[1;32mModelo editado com sucesso!\033[m")

            elif escolha == 3:
                print("\n\033[1;34mEditando Placa do Veículo\033[m\n")
                nova_placa = input("Digite a placa do veículo: ").upper().strip()

                for dados in cliente.values():
                    for dado in dados.values():
                        dado["idade"] = dado["idade"]
                        dado["carro"] = dado["carro"]
                        dado["placa"] = nova_placa
                        dado["credito"] = dado["credito"]

                with open("clientes.json","w",encoding="utf-8") as arquivo:
                    json.dump(clientes,arquivo,indent=4)
                
                print("\033[1;32mPlaca editada com sucesso!\033[m")

            elif escolha == 4:
                print("\n\033[1;34mEditando dados de cadastro:\033[m\n")
                novo_idade = int(input("Digite sua idade: "))
                novo_carro = input("Digite o modelo do veículo: ").upper().strip()
                nova_placa = input("Digite a placa do veículo: ").upper().strip()

                for dados in cliente.values():
                    for dado in dados.values():
                        dado["idade"] = novo_idade
                        dado["carro"] = novo_carro
                        dado["placa"] = nova_placa
                        dado["credito"] = dado["credito"]

                with open("clientes.json","w",encoding="utf-8") as arquivo:
                    json.dump(clientes,arquivo,indent=4)
                
                print("\033[1;32mDados editados com sucesso!\033[m")

            else:
                print("\033[1;31mEscolha 0, 1, 2 ,3 , 4 para ser uma escolha válida!\033[m")
        except ValueError:
            print("\033[1;31mDigite um valor válido!\033[m")
        except Exception:
            print("\033[1;31mOcorreu um erro inesperado!\033[m")


#  ///////////////// ATUALIZAÇÃO DA LISTA /////////////////////////////////////////////////////////////

def atualizarListaClientes() -> None:
    """
    Retorna a lista de clientes atualizada com os novos clientes cadastrados no arquivo json. A atualização é necessária para que o novo usuário cadastrado consiga fazer login utilizando seu token.
    """

    lista_de_clientes = []

    with open("clientes.json","r") as arquivo:
        lista = json.load(arquivo)

    for item in lista:
        lista_de_clientes.append(item)

    with open("clientes.json","w",encoding="utf-8") as arquivo:
        json.dump(lista_de_clientes,arquivo,indent=4,ensure_ascii=False)

    return lista_de_clientes
    