import requests

def get_all_stats():
    resp = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    data = resp.json()
    return data["elements"]
