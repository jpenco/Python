# Lista para armazenar os dados
dados = []

# Função para criar um novo item
def criar():
    novo_item = input("Digite o novo item: ")
    dados.append(novo_item)
    print("Item criado com sucesso.")

# Função para ler todos os itens
def ler():
    if not dados:
        print("Nenhum item encontrado.")
    else:
        for i, item in enumerate(dados, start=1):
            print(f"{i}. {item}")

# Função para atualizar um item
def atualizar():
    ler()
    indice = int(input("Digite o índice do item a ser atualizado: ")) - 1
    if 0 <= indice < len(dados):
        novo_valor = input("Digite o novo valor: ")
        dados[indice] = novo_valor
        print("Item atualizado com sucesso.")
    else:
        print("Índice inválido.")

# Função para deletar um item
def deletar():
    ler()
    indice = int(input("Digite o índice do item a ser deletado: ")) - 1
    if 0 <= indice < len(dados):
        del dados[indice]
        print("Item deletado com sucesso.")
    else:
        print("Índice inválido.")

# Menu principal
while True:
    print("\nMenu:")
    print("1. Criar novo item")
    print("2. Ler todos os itens")
    print("3. Atualizar um item")
    print("4. Deletar um item")
    print("5. Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        criar()
    elif escolha == "2":
        ler()
    elif escolha == "3":
        atualizar()
    elif escolha == "4":
        deletar()
    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
