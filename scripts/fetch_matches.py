import requests
import json

def fetch_vitality_matches():
    url = "https://hltv-api-two.vercel.app/api/team/9565"
    response = requests.get(url)

    try:
        data = response.json()
    except:
        return []

    matches = []

    for match in data.get("matches", []):
        matches.append({
            "id": match.get("id"),
            "team1": match.get("team1", {}).get("name"),
            "team2": match.get("team2", {}).get("name"),
            "date": match.get("date"),
            "event": match.get("event", {}).get("name"),
            "format": match.get("format"),
            "result": match.get("result")
        })

    return matches

if __name__ == "__main__":
    print(json.dumps(fetch_vitality_matches(), indent=2))
