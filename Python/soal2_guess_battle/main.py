from game import play_level
from scoreboard import *

from colorama import init
from colorama import Fore

init(autoreset=True)

print(
    Fore.CYAN +
    "================================"
)

print(
    Fore.CYAN +
    "      GUESS BATTLE GAME"
)

print(
    Fore.CYAN +
    "================================"
)

nama = input(
    Fore.YELLOW +
    "Masukkan nama pemain: "
)

total_skor = 0

# LEVEL 1
total_skor += play_level(
    1,
    10,
    3
)

# LEVEL 2
total_skor += play_level(
    2,
    50,
    5
)

# LEVEL 3
total_skor += play_level(
    3,
    100,
    7
)

print(
    Fore.GREEN +
    f"\nTotal skor kamu: {total_skor}"
)

scores = load_scores()

scores.append({
    "nama": nama,
    "score": total_skor
})

save_scores(scores)

tampilkan_top5(scores)