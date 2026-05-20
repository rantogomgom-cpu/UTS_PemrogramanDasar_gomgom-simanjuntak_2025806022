import csv
import json

data = []

with open("../C/data_mahasiswa.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append({
            "nama": row["Nama"],
            "nim": row["NIM"],
            "nilai_akhir": row["NilaiAkhir"],
            "mutu": row["Mutu"]
        })

with open("data_mahasiswa.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("Konversi selesai!")