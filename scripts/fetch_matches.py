import requests
import json

def fetch_vitality_matches():
    url = "https://hltv-api.vercel.app/api/team/9565"  # Team Vitality ID
    data = requests.get(url).json()

    matches = []

    for match in data.get("matches", []):
        if match.get("event", {}).get("name"):
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
