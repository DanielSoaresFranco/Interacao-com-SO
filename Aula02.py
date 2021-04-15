# Para pegar informações sobre a máquina utilizada, usar os.environ(colchetes opcionais para filtrar dados)
# Para pegar o processo atual usar os.getpid()
import os
print(os.environ['APPDATA'])
print(os.getpid())
