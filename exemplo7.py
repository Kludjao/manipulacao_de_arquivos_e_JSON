import json

# carrega os dados do arquivo json para uma estrutura do python
with open('cadastro.json', 'r') as arquivo:
    lista = json.load(arquivo)

# percorre todos os clientes do arquivo json
for cliente in lista:
    print('------------------------------')
    print(f'CPF: {cliente["cpf"]}')
    print(f'Nome: {cliente["nome"]}')
    print(f'Idade: {cliente["idade"]}')

# realiza uma busca por um cliente específico
nome = input('Digite um nome para buscar: ')
for cliente in lista:
    if cliente['nome'] == nome:
        print(f'CPF: {cliente["cpf"]}')
        print(f'Nome: {cliente["nome"]}')
        print(f'Idade: {cliente["idade"]}')