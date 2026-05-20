import random

def play(level):
    if level == 1:
        max_num = 10
        kesempatan = 3
    elif level == 2:
        max_num = 50
        kesempatan = 5
    else:
        max_num = 100
        kesempatan = 7

    angka = random.randint(1, max_num)

    while kesempatan > 0:
        try:
            tebakan = int(input(f"Tebak angka 1-{max_num}: "))

            if tebakan == angka:
                print("Benar!")
                return kesempatan * 10

            elif tebakan < angka:
                print("Terlalu kecil!")

            else:
                print("Terlalu besar!")

            kesempatan -= 1

        except:
            print("Input harus angka!")

    return 0