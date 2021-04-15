import os
import shutil

# Para deletar um arquivo usar os.remove(local do arquivo)
os.remove('teste\\pasta2\\arquivo2.txt')

# Para deletar diretórios vazios podemos usar os.removedirs(local do diretório)
os.removedirs('teste\\a')

# Para deletar diretórios que tenham algum arquivo/diretório usar shutil.rmtree(local do arquivo)
shutil.rmtree('teste\\pasta3')
