import os

print("Iniciando pipeline")
os.system("python extract.py")

print("Transformando dados")
os.system("python transform.py")

print("Carregando dados")
os.system("python load.py")
