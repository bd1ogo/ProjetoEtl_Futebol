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

print("\nTimes com mais gols feitos")
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

print("\nTimes com mais gols sofridos")
for linha in resultado_sofridos:
    print(linha)

cursor.execute("""
    SELECT
        feitos.time,
        feitos.gols_feitos,
        sofridos.gols_sofridos
    FROM(
        SELECT time, SUM(gols) AS gols_feitos
        FROM (
            SELECT mandante AS time, gols_mandante AS gols FROM jogos
            UNION ALL
            SELECT visitante AS time, gols_visitante AS gols FROM jogos
            ) AS tabela
            GROUP BY time
        ) AS feitos
        JOIN (
            SELECT time, SUM(gols) AS gols_sofridos
            FROM (
                SELECT mandante AS time, gols_visitante AS gols FROM jogos
                UNION ALL
                SELECT visitante AS time, gols_mandante AS gols FROM jogos
            ) AS tabela
            GROUP BY time
        ) AS sofridos
        ON feitos.time = sofridos.time
        ORDER BY feitos.gols_feitos DESC, sofridos.gols_sofridos ASC
""")
resultado = cursor.fetchall()

print("\nRanking de Times")
for linha in resultado:
    print(linha)

ranking = []
for linha in resultado:
    ranking.append({
        "time": linha[0],
        "gols_feitos": linha[1],
        "gols_sofridos": linha[2]
    })

with open("data/ranking.json", "w", encoding="utf-8") as f:
    json.dump(ranking, f, indent=4, default=int)

print("Análise concluída")
