from game import play
from scoreboard import save_score, top_score

nama = input("Masukkan nama pemain : ")

total = 0

for level in range(1, 4):
    print(f"\nLEVEL {level}")
    total += play(level)

print(f"\nTotal skor : {total}")

save_score(nama, total)

top_score()