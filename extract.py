import requests
import json
from datetime import datetime

url = "https://www.thesportsdb.com/api/v1/json/3/eventspastleague.php?id=4328"

response = requests.get(url)
response.status_code

data = response.json()

jogos = []

for event in data["events"]:
    league = event["strLeague"]
    home = event["strHomeTeam"]
    away = event["strAwayTeam"]
    home_score = event["intHomeScore"] or 0
    away_score = event["intAwayScore"] or 0
    date = datetime.strptime(event["dateEvent"], "%Y-%m-%d")

    jogo = {
        "liga": league,
        "data": date.strftime("%Y-%m-%d"),
        "mandante": home,
        "visitante": away,
        "gols_mandante": home_score,
        "gols_visitante": away_score
    }

    jogos.append(jogo)
    print(jogo)

with open("data/jogos.json", "w") as f:
    json.dump(jogos, f, indent=4)
