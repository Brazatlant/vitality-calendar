import json
from datetime import datetime

def generate_event(match):
    uid = f"VITALITY-{match['id']}"
    summary = f"{match['team1']} vs {match['team2']} – {match['event']}"

    if match["result"]:
        summary = f"{match['team1']} {match['result']} {match['team2']} – {match['event']}"

    dtstart = datetime.utcfromtimestamp(match["date"] / 1000).strftime("%Y%m%dT%H%M%SZ")
    dtend = datetime.utcfromtimestamp(match["date"] / 1000 + 7200).strftime("%Y%m%dT%H%M%SZ")

    return f"""
BEGIN:VEVENT
UID:{uid}
SUMMARY:{summary}
DTSTART:{dtstart}
DTEND:{dtend}
DESCRIPTION:Match Vitality CS2 – {match['event']}
END:VEVENT
"""

def generate_calendar(matches):
    events = "".join(generate_event(m) for m in matches)

    return f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Brazatlant//Vitality CS2 Auto Calendar//FR
CALSCALE:GREGORIAN
METHOD:PUBLISH
{events}
END:VCALENDAR
"""

if __name__ == "__main__":
    matches = json.load(open("matches.json"))
    print(generate_calendar(matches))
