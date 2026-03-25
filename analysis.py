import json
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    port = 3307,
    user = "user",
    password = "password"
)

cursor = conexao.cursor()
conexao.database = "futebol"

cursor.execute("""
    SELECT time, SUM(gols) AS total_gols
    FROM (
        SELECT mandante AS time, gols_mandante AS gols FROM jogos
        UNION ALL
        SELECT visitante AS time, gols_visitante AS gols FROM jogos
    ) AS tabela
    GROUP BY time
    ORDER BY total_gols DESC
""")
resultado_feitos = cursor.fetchall()

print("\n=== Times com mais gols feitos ===")
for linha in resultado_feitos:
    print(linha)

cursor.execute("""
    SELECT time, SUM(gols) AS total_gols
    FROM (
        SELECT mandante AS time, gols_visitante AS gols FROM jogos
        UNION ALL
        SELECT visitante AS time, gols_mandante AS gols FROM jogos
    ) AS tabela
    GROUP BY time
    ORDER BY total_gols DESC
""")
resultado_sofridos = cursor.fetchall()

print("\n=== Times com mais gols sofridos ===")
for linha in resultado_sofridos:
    print(linha)
