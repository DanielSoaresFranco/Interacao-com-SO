import shutil

# Para copiarmos um arquivo para outro lugar usar shutil.copy2(local do arquivo, local da cópia(não enviando nome do arquivo fica o nome original))
shutil.copy2('pasta1\\arquivo2.txt', 'pasta2\\')
