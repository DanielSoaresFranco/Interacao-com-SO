import os

# Para verificar se uma pasta existe usar os.path.isdir(local da pasta)
if (not os.path.isdir('desafio/desafio_1')):
    os.makedirs('desafio/desafio_1')
else:
    print('pastas já existem')

# Para verificar se arquivo existe usar os.path.isfile(local do arquivo)
if (not os.path.isfile('desafio/arquivo.txt')):
    print('Arquivo não existe')
else:
    print('Arquivo existe')

# Para verificar se existe(em qualquer formato) usar os.path.exists(local do arquivo/diretório)
if (not os.path.exists('desafio/desafio_1')):
    os.makedirs('desafio/desafio_1')
else:
    print('pastas já existem')
if (not os.path.exists('desafio/arquivo.txt')):
    print('Arquivo não existe')
else:
    print('Arquivo existe')
