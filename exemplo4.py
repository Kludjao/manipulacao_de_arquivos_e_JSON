# abre o arquivo para leitura
with open('nomes.txt', 'r') as arquivo:

    # percorrer as linhas do arquivo
    for linha in arquivo.readlines():

        # gera uma lista com os dados da string separados por vírgula
        lista = linha.split(',')

        print(f'CPF: {lista[0]}')
        print(f'Nome: {lista[1]}')
        print(f'Idade: {lista[2]}')
