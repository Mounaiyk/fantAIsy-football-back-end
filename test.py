import requests

response = requests.get(f"https://fantasy.premierleague.com/api/element-summary/1/")
print(response.json()["history"][-1]["value"])
