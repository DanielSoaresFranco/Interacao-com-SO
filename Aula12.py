import os
import shutil

diretorio = 'desafio'
num_pastas_arq = int(input('Quantas pastas e arquivos? '))

if os.path.exists(diretorio):
    shutil.rmtree(diretorio)
os.mkdir(diretorio)

for c in range(0, num_pastas_arq):
    if not os.path.exists(f'{diretorio}\\pasta_{c + 1}'):
        os.mkdir(f'{diretorio}\\pasta_{c + 1}')
    for c2 in range(0, num_pastas_arq):
        open(f'{diretorio}\\pasta_{c + 1}\\arquivo_{c2 + 1}.txt', 'w+')