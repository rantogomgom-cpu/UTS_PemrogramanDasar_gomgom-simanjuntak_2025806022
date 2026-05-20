def save_report(data):

    with open("report.txt", "w") as f:

        f.write(f"Jumlah baris : {data['baris']}\n")
        f.write(f"Jumlah kata : {data['kata']}\n")

        f.write("\nTop 5 Kata:\n")

        for kata, jumlah in data['top5']:
            f.write(f"{kata} {'#' * jumlah}\n")

        f.write(f"\nVokal : {data['vokal']}\n")
        f.write(f"Konsonan : {data['konsonan']}\n")