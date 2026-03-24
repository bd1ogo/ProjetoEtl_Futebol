import json
from datetime import datetime

with open("data/jogos.json", "r", encoding="utf-8") as f:
    data = json.load(f)

jogos_tratados=[]

for event in data["events"]:
    jogo = {
        "liga": event["strLeague"],
        "data": datetime.strptime(event["dateEvent"], "%Y-%m-%d").strftime("%Y-%m-%d %H-%M-%S"),
        "mandante": event["strHomeTeam"],
        "visitante": event["strAwayTeam"],
        "gols_mandante": event["intHomeScore"] or 0,
        "gols_visitante": event["intAwayScore"] or 0
    }
    jogos_tratados.append(jogo)

with open("data/jogos_tratados.json", "w", encoding="utf-8") as f:
    json.dump(jogos_tratados, f, indent=4)

print("Transformação concluída!")