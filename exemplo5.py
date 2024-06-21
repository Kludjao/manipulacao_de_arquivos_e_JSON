
# criar um arquivo de texto
with open('cadastro de cliente.txt', 'w') as arquivo:
    # cadastra varios cliente até informar cpf -1
    while True:
        cpf = input('CPF: ')
        if cpf == '-1':
            break                       # finaliza o loop
        nome = input('Nome: ')
        idade = int(input('Idade: '))

        # escreve os dados no arquivo de texto
        arquivo.write(f'{cpf},{nome},{idade}\n')
