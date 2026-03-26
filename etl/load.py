import json
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    port = 3307,
    user = "user",
    password = "password"
)

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS futebol")
conexao.database = "futebol"

cursor.execute("""
CREATE TABLE IF NOT EXISTS jogos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    liga VARCHAR(200),
    mandante VARCHAR(100),
    visitante VARCHAR(100),
    gols_mandante INT,
    gols_visitante INT,
    data DATETIME
)
""")

with open("data/jogos_tratados.json", "r", encoding="utf-8") as f:
    jogos = json.load(f)

for jogo in jogos:
    sql = """
    INSERT INTO jogos(liga, mandante, visitante, gols_mandante, gols_visitante, data)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        jogo["liga"],
        jogo["mandante"],
        jogo["visitante"],
        jogo["gols_mandante"],
        jogo["gols_visitante"],
        jogo["data"]
    )
    cursor.execute(sql, valores)

conexao.commit()
print("Dados inseridos com sucesso!")

cursor.close()
conexao.close()