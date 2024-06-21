import json

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

print(lista_clientes)

# salva os dados em um arquivo json
with open('cadastro.json', 'w') as arquivo:
    json.dump(lista_clientes, arquivo, indent=4, ensure_ascii=False)
