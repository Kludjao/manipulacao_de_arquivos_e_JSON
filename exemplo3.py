# abre o arquivo para leitura
arquivo = open('nomes.txt', 'r')

# copiar o conteudo do aruivo para uma única string
texto = arquivo.read()
print(texto)

# fecha o arquivo
arquivo.close()

