#  Interagindo com o sistema operacional
#  Para interagir com o SO precisamos do pacote OS
#  Também podemos pegar  através do namespace platform, usando platform.system
import os
import platform
n1 = os.name
n2 = platform.system()
print(n1, n2)
