from collections import Counter
from utils import hitung_vokal_konsonan

def analyze_text(filename):

    with open(filename, "r") as file:

        text = file.read().lower()

    # Jumlah baris
    lines = text.splitlines()

    # Jumlah kata
    words = text.split()

    # Frekuensi kata
    frekuensi = Counter(words)

    # Top 5 kata
    top5 = frekuensi.most_common(5)

    # Hitung vokal dan konsonan
    vokal, konsonan = \
        hitung_vokal_konsonan(text)

    # Membuat report
    with open("report.txt", "w") as report:

        report.write(
            "===== HASIL ANALISIS =====\n\n"
        )

        report.write(
            f"Jumlah Baris : {len(lines)}\n"
        )

        report.write(
            f"Jumlah Kata : {len(words)}\n"
        )

        report.write(
            f"Jumlah Huruf Vokal : {vokal}\n"
        )

        report.write(
            f"Jumlah Huruf Konsonan : {konsonan}\n\n"
        )

        report.write(
            "===== TOP 5 KATA =====\n"
        )

        for kata, jumlah in top5:

            report.write(
                f"{kata} : {jumlah}\n"
            )

        report.write(
            "\n===== GRAFIK ASCII =====\n"
        )

        for kata, jumlah in top5:

            report.write(
                f"{kata} {'#' * jumlah}\n"
            )

    print("Report berhasil dibuat!")