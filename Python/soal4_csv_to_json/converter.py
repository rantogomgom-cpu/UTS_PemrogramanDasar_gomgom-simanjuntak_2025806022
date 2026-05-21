import csv
import json

def convert_data():

    data = []

    total_nilai = 0
    jumlah_mahasiswa = 0

    print("\n======================================")
    print("DATA MAHASISWA")
    print("======================================")

    with open(
        "data_mahasiswa.csv",
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            print(
                f"Nama : {row['Nama']}"
            )

            print(
                f"NIM : {row['NIM']}"
            )

            print(
                f"Nilai Akhir : "
                f"{row['NilaiAkhir']}"
            )

            print(
                f"Mutu : {row['Mutu']}"
            )

            print("----------------------------------")

            total_nilai += \
                float(row['NilaiAkhir'])

            jumlah_mahasiswa += 1

            data.append({

                "nama":
                    row["Nama"],

                "nim":
                    row["NIM"],

                "nilai_akhir":
                    float(
                        row["NilaiAkhir"]
                    ),

                "mutu":
                    row["Mutu"]
            })

    rata_rata = \
        total_nilai / jumlah_mahasiswa

    print(
        f"\nRata-rata Nilai Akhir : "
        f"{rata_rata:.2f}"
    )

    with open(
        "data_mahasiswa.json",
        "w"
    ) as json_file:

        json.dump(
            data,
            json_file,
            indent=4
        )

    print(
        "\nData berhasil dikonversi "
        "ke JSON!"
    )