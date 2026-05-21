def hitung_vokal_konsonan(text):

    vokal = "aiueo"

    jumlah_vokal = 0
    jumlah_konsonan = 0

    for huruf in text:

        if huruf.isalpha():

            if huruf.lower() in vokal:
                jumlah_vokal += 1

            else:
                jumlah_konsonan += 1

    return jumlah_vokal, jumlah_konsonan