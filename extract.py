import requests
import json

url = "https://www.thesportsdb.com/api/v1/json/3/eventspastleague.php?id=4328"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("data/jogos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Dados extraídos com sucesso!")
else:
    print(f"Erro na requisição: {response.status_code}")