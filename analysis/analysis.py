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

cursor.execute("""
    SELECT 
        time,
        SUM(gols_feitos) AS gols_feitos,
        SUM(gols_sofridos) AS gols_sofridos,
        SUM(gols_feitos) - SUM(gols_sofridos) AS saldo_gols
    FROM (
        SELECT 
            mandante AS time,
            gols_mandante AS gols_feitos,
            gols_visitante AS gols_sofridos
    FROM jogos
    UNION ALL
    SELECT 
        visitante AS time,
        gols_visitante AS gols_feitos,
        gols_mandante AS gols_sofridos
    FROM jogos
    ) AS tabela
    GROUP BY time
    ORDER BY saldo_gols DESC, gols_feitos DESC
""")
resultado = cursor.fetchall()

ranking = []
for linha in resultado:
    ranking.append({
        "time": linha[0],
        "saldo_gols": linha[1],
        "gols_feitos": linha[2],
        "gols_sofridos": linha[3]
    })

with open("data/ranking.json", "w", encoding="utf-8") as f:
    json.dump(ranking, f, indent=4, default=int)

print("Análise concluída")
