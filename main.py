import os

print("Iniciando Pipeline")
os.system("python extract.py")

print("Transformando Dados")
os.system("python transform.py")

print("Carregando Dados")
os.system("python load.py")

print("Analisando Dados")
os.system("python analysis.py")

print("Carregando Dashboard")
os.system("streamlit run dashboard.py")

print("\n Pipeline Finalizado")