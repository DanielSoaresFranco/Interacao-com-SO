from random import randint

caracteres = ['QWERTYUIOPASDFGHJKLZXCVBNM', 'qwertyuiopasdfghjklzxcvbnm', '!@#$%&*()', '1234567890']
senha = ''

for c in range(0, randint(8, 20)):
    tipo = randint(0, 3)
    tam = len(caracteres[tipo])
    senha += caracteres[tipo][randint(0, tam - 1)]
print(f'Sua senha é: \n{senha}')
