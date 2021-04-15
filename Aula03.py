import os

# Para pegar o diretório atual usar os.getcwd()
print('Diretório atual: ', os.getcwd())

# Para ver o diretório do arquivo usar os.path()
# Para referenciar o arquivo atual, usar __file__ na função
print('Arquivo Atual:', __file__)

#para nome do arquivo usar os.path.basename()
print('Nome do arquivo atual: ', os.path.basename(__file__))

# Para pegar a pasta do arquivo atual usar os.path.dirname()
print('Pasta do arquivo atual: ', os.path.dirname(__file__))

# Para pegar caminho absoluto atual usar os.path.abspath()
print('Caminho absoluto: ', os.path.abspath(__file__))
