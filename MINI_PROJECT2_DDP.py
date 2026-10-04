import datetime
import os
from prettytable import PrettyTable

akun = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

data = {
    1: {
        "nama": "Jayu",
        "profesi": "Dokter",
        "unit": "Poli Umum"
    },
    2: {
        "nama": "AzamLevis",
        "profesi": "Perawat",
        "unit": "UGD"
    }
}

def login():
    print("=== LOGIN ===")

    username = input("Username : ")
    password = input("Password : ")

    if username in akun and akun[username]["password"] == password:
        print("Login berhasil!")
        return username, akun[username]["role"]
    else:
        print("Username atau password salah!")
        return None, None

def tampil_data():
    print("\n=== DATA DOKTER & PERAWAT ===")

    if len(data) == 0:
        print("Belum ada data.")
    else:
        tabel = PrettyTable()

        tabel.field_names = [
            "No",
            "Nama",
            "Profesi",
            "Unit Kerja"
        ]

        for nomor, item in data.items():
            tabel.add_row([
                nomor,
                item["nama"],
                item["profesi"],
                item["unit"]
            ])

        print(tabel)

def tambah_data():
    print("\n=== TAMBAH DATA ===")

    nama = input("Nama : ")
    profesi = input("Profesi (Dokter/Perawat) : ")
    unit = input("Unit Kerja : ")

    if nama == "" or profesi == "" or unit == "":
        print("Data tidak boleh kosong!")
        return

    profesi = profesi.lower()

    if profesi != "dokter" and profesi != "perawat":
        print("Profesi harus Dokter atau Perawat!")
        return

    nomor = max(data.keys(), default=0) + 1

    data[nomor] = {
        "nama": nama,
        "profesi": profesi.capitalize(),
        "unit": unit
    }

    print("Data berhasil ditambahkan.")

def ubah_data():
    tampil_data()

    try:
        nomor = int(input("\nMasukkan nomor data yang diubah: "))

        if nomor not in data:
            print("Nomor data tidak ditemukan!")
            return

        nama = input("Nama baru : ")
        profesi = input("Profesi baru (Dokter/Perawat) : ")
        unit = input("Unit kerja baru : ")

        if nama == "" or profesi == "" or unit == "":
            print("Data tidak boleh kosong!")
            return

        profesi = profesi.lower()

        if profesi != "dokter" and profesi != "perawat":
            print("Profesi harus Dokter atau Perawat!")
            return

        data[nomor] = {
            "nama": nama,
            "profesi": profesi.capitalize(),
            "unit": unit
        }

        print("Data berhasil diubah.")

    except ValueError:
        print("Nomor harus berupa angka!")

def hapus_data():
    tampil_data()

    try:
        nomor = int(input("\nMasukkan nomor data yang dihapus: "))

        if nomor in data:
            del data[nomor]
            print("Data berhasil dihapus.")
        else:
            print("Nomor data tidak ditemukan!")

    except ValueError:
        print("Nomor harus berupa angka!")

def main():
    while True:
        username, role = login()

        if username is not None:
            break

    while True:

        os.system("cls" if os.name == "nt" else "clear")

        print("======================================")
        print("SISTEM PENDATAAN UNIT KERJA")
        print("DOKTER & PERAWAT")
        print("======================================")
        print("Tanggal :", datetime.date.today())
        print("Login sebagai :", role)

        print("\n1. Lihat Data")

        if role == "admin":
            print("2. Tambah Data")
            print("3. Ubah Data")
            print("4. Hapus Data")

        print("0. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            tampil_data()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2" and role == "admin":
            tambah_data()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "3" and role == "admin":
            ubah_data()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "4" and role == "admin":
            hapus_data()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak valid!")
            input("\nTekan Enter untuk kembali...")


main()