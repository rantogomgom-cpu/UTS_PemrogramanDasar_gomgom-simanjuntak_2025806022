import random
from colorama import Fore

def play_level(level, max_num, attempts):

    print(Fore.CYAN + f"\n===== LEVEL {level} =====")
    print(Fore.YELLOW +
          f"Tebak angka 1 sampai {max_num}")

    angka = random.randint(1, max_num)

    while attempts > 0:

        try:
            tebakan = int(
                input("Masukkan tebakan: ")
            )

            if tebakan == angka:

                print(
                    Fore.GREEN +
                    "Tebakan BENAR!"
                )

                skor = attempts * 10

                print(
                    Fore.GREEN +
                    f"Skor level: {skor}"
                )

                return skor

            elif tebakan < angka:

                print(
                    Fore.RED +
                    "Terlalu kecil!"
                )

            else:

                print(
                    Fore.RED +
                    "Terlalu besar!"
                )

            attempts -= 1

            print(
                Fore.MAGENTA +
                f"Sisa percobaan: {attempts}"
            )

        except:

            print(
                Fore.RED +
                "Input harus angka!"
            )

    print(
        Fore.RED +
        f"Kalah! Jawabannya adalah {angka}"
    )

    return 0