#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Mahasiswa {
    char nama[50];
    char nim[20];
    float tugas, uts, uas, akhir;
    char mutu;
    struct Mahasiswa *next;
};

typedef struct Mahasiswa Mhs;

Mhs *head = NULL;

float hitungNilai(float tugas, float uts, float uas) {
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas);
}

char hitungMutu(float nilai) {
    if (nilai >= 85) return 'A';
    else if (nilai >= 70) return 'B';
    else if (nilai >= 60) return 'C';
    else if (nilai >= 50) return 'D';
    else return 'E';
}

void tambahData() {
    Mhs *baru = (Mhs*) malloc(sizeof(Mhs));

    printf("Nama : ");
    scanf(" %[^\n]", baru->nama);

    printf("NIM : ");
    scanf("%s", baru->nim);

    printf("Nilai Tugas : ");
    scanf("%f", &baru->tugas);

    printf("Nilai UTS : ");
    scanf("%f", &baru->uts);

    printf("Nilai UAS : ");
    scanf("%f", &baru->uas);

    baru->akhir = hitungNilai(baru->tugas, baru->uts, baru->uas);
    baru->mutu = hitungMutu(baru->akhir);
    baru->next = NULL;

    if (head == NULL) {
        head = baru;
    } else {
        Mhs *temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = baru;
    }

    printf("Data berhasil ditambahkan!\n");
}

void tampilData() {
    Mhs *temp = head;

    printf("\n=== DATA MAHASISWA ===\n");

    while (temp != NULL) {
        printf("%s | %s | %.2f | %c\n",
               temp->nama,
               temp->nim,
               temp->akhir,
               temp->mutu);

        temp = temp->next;
    }
}

void cariData() {
    char cari[20];

    printf("Masukkan NIM : ");
    scanf("%s", cari);

    Mhs *temp = head;

    while (temp != NULL) {
        if (strcmp(temp->nim, cari) == 0) {
            printf("Data ditemukan!\n");
            printf("%s | %s | %.2f | %c\n",
                   temp->nama,
                   temp->nim,
                   temp->akhir,
                   temp->mutu);
            return;
        }

        temp = temp->next;
    }

    printf("Data tidak ditemukan!\n");
}

void hapusData() {
    char cari[20];
-----------------------------===================================----------------------------
    printf("Masukkan NIM yang akan dihapus : ");
    scanf("%s", cari);

    Mhs *temp = head;
    Mhs *prev = NULL;

    while (temp != NULL) {
        if (strcmp(temp->nim, cari) == 0) {

            if (prev == NULL)
                head = temp->next;
            else
                prev->next = temp->next;

            free(temp);

            printf("Data berhasil dihapus!\n");
            return;
        }

        prev = temp;
        temp = temp->next;
    }

    printf("Data tidak ditemukan!\n");
}

void simpanCSV() {
    FILE *fp = fopen("data_mahasiswa.csv", "w");

    fprintf(fp, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");

    Mhs *temp = head;

    while (temp != NULL) {
        fprintf(fp, "%s,%s,%.2f,%.2f,%.2f,%.2f,%c\n",
                temp->nama,
                temp->nim,
                temp->tugas,
                temp->uts,
                temp->uas,
                temp->akhir,
                temp->mutu);

        temp = temp->next;
    }

    fclose(fp);

    printf("Data berhasil disimpan ke CSV!\n");
}

int main() {
    int pilih;

    do {
        printf("\n=== MENU ===\n");
        printf("1. Tambah Data\n");
        printf("2. Tampil Data\n");
        printf("3. Cari Data\n");
        printf("4. Hapus Data\n");
        printf("5. Simpan CSV\n");
        printf("0. Keluar\n");

        printf("Pilih : ");
        scanf("%d", &pilih);

        switch(pilih) {
            case 1: tambahData(); break;
            case 2: tampilData(); break;
            case 3: cariData(); break;
            case 4: hapusData(); break;
            case 5: simpanCSV(); break;
        }

    } while(pilih != 0);

    return 0;
}