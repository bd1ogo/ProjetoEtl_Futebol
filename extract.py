import requests
import json

url = "https://www.thesportsdb.com/api/v1/json/3/eventspastleague.php?id=4328"

response = requests.get(url)
response.status_code

data = response.json()
print(data)

jogos = []

for event in data["events"]:
    home = event["strHomeTeam"]
    away = event["strAwayTeam"]
    home_score = event["intHomeScore"] or 0
    away_score = event["intAwayScore"] or 0
    date = event["dateEvent"]

    jogo = {
        "data": date,
        "mandante": home,
        "visitante": away,
        "placar": f"{home_score} x {away_score}"
    }

    jogos.append(jogo)
    print(jogos)

with open("jogos.json", "w") as f:
    json.dump(jogos, f, indent=4)
