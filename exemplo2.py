# lista vazia
lista_clientes = []

# cadastra os cliente
for i in range(3):
    cpf = input('CPF: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))

    # cria um dicionario com os dados os clientes
    cliente = {'cpf': cpf,
               'nome': nome,
               'idade': idade}

    # insere o dicionario na lista
    lista_clientes.append(cliente)

# percorre os dicionários da lista
for cliente in lista_clientes:
    print('-----------------------------')
    print(f'CPF: {cliente["cpf"]}')
    print(f'Nome: {cliente["nome"]}')
    print(f'Idade: {cliente["idade"]}')
