# exemplo de dicionário
pessoa = {'name': 'Paulo',
          'age': 30,
          'job': 'Professor'}

# consulta a um item do dicionário
print(pessoa['name'])
print(pessoa['age'])

# altera um item do dicionario
pessoa['name'] = 'Paulo Vieira'
pessoa['age'] = 35

# inserir um item
pessoa['cpf'] = 1234567
print(pessoa)

# excluir um item
pessoa.pop('job')
print(pessoa)

# percorrer todas as chaves do dicionario
for chave in pessoa.keys():
    print(chave)

# percorrer todos os valores do dicionário
for valor in pessoa.values():
    print(valor)

# percorrer todos os itens (chave e valor)  do dicionario
for chave, valor in pessoa.items():
    print(chave, valor)

# buscar uma chave no dicionario (in)
chave = input('Digite uma chave para buscar no dicionário: ')
if chave in pessoa:
    print('A chave existe no dicionário.')
    print(f'Nome: {pessoa[chave]}')
else:
    print('A chave não existe no dicionário')
