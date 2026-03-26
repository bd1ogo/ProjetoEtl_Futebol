import os

print("Iniciando Pipeline")
os.system("python etl/extract.py")

print("Transformando Dados")
os.system("python etl/transform.py")

print("Carregando Dados")
os.system("python etl/load.py")

print("Analisando Dados")
os.system("python analysis/analysis.py")

print("Carregando Dashboard")
os.system("streamlit run dashboard/dashboard.py")

print("\n Pipeline Finalizado")