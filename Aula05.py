import os

# Para criar uma pasta, usamos os.mkdir(caminho da pasta com nome), ele só cria se não existir pasta
os.mkdir('teste')

# os.mkdir() Não funciona com recursividadde

# Para usar com recursividade, usar os.makedirs(caminho das pastas)
os.makedirs('teste 1\\teste 1.1')

for d in range(0, 5):
    try:
        os.mkdir(f"teste {d + 1}")
    except FileExistsError:
        print(f'Não foi possível criar pasta {f"teste {d + 1}"}')
    else:
        print(f'Pasta {f"teste {d + 1}"} criada com sucesso!')
print('Processo finalizado. Volte sempre!')
