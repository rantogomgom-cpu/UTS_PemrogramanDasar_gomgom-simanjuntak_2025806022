import json
from colorama import Fore

def load_scores():

    try:

        with open(
            "scores.json",
            "r"
        ) as file:

            return json.load(file)

    except:

        return []

def save_scores(scores):

    with open(
        "scores.json",
        "w"
    ) as file:

        json.dump(
            scores,
            file,
            indent=4
        )

def tampilkan_top5(scores):

    scores = sorted(
        scores,
        key=lambda x: x["score"],
        reverse=True
    )

    print(
        Fore.CYAN +
        "\n===== TOP 5 SCORE ====="
    )

    for i, pemain in enumerate(
        scores[:5],
        start=1
    ):

        print(
            Fore.YELLOW +
            f"{i}. "
            f"{pemain['nama']} "
            f"- "
            f"{pemain['score']} pts"
        )