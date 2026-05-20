import json
import os

FILE = "scores.json"

def save_score(nama, skor):

    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append({
        "nama": nama,
        "skor": skor
    })

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def top_score():

    if not os.path.exists(FILE):
        return

    with open(FILE, "r") as f:
        data = json.load(f)

    data = sorted(data, key=lambda x: x['skor'], reverse=True)

    print("\n=== TOP SCORE ===")

    for i, d in enumerate(data[:5], start=1):
        print(f"{i}. {d['nama']} - {d['skor']} pts")