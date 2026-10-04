# MINIPROJECT2_DDP_RAKHMAT NUR ALIF ABDILLAH
# SISTEM PENDATAAAN UNIT KERJA DOKTER & PERAWAT 

NAMA : RAKHMAT NUR ALIF ABDILLAH <br>
NIM : 2609116100 <br>
KELAS : C

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 8_49_06 PM" src="https://github.com/user-attachments/assets/8a0f5828-fba2-4c19-acd2-3d9f700456e6" />

import datetime
import os
from prettytable import PrettyTable

- datetime dipakai untuk mengambil tanggal hari ini.
- os dipakai untuk membersihkan layar terminal supaya tampilan menu selalu rapi.
- PrettyTable dipakai untuk membuat tabel yang rapi, jadi data tidak tampil berantakan.

akun = {"admin": {...}, "user": {...}}
data = {1: {...}, 2: {...}}

- akun berisi daftar orang yang boleh masuk. Isinya username, password, dan jabatannya (role).
- data berisi daftar dokter dan perawat. Tiap orang punya nomor, lalu nama, profesi, dan unit kerja. Contohnya nomor 1 adalah Jayu, seorang dokter di Poli Umum.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 8_49_21 PM" src="https://github.com/user-attachments/assets/9f41ed79-b386-4ed2-93a3-12e09349335d" />

Fungsi login() : Fungsi ini menanyakan username dan password, lalu mencocokkannya dengan akun.
- Kalau cocok, kamu dipersilakan masuk dan program mencatat siapa kamu (admin atau user).
- Kalau salah, muncul pesan "salah" dan kamu diminta mengulang.

Fungsi tampil_data(): menampilkan daftar
- Kalau data masih kosong, muncul tulisan "Belum ada data."
- Kalau ada isinya, program membuat tabel dengan kolom No, Nama, Profesi, dan Unit Kerja. Lalu program mengambil data satu per satu dan memasukkannya ke tabel (itu fungsi for dan add_row).

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 8_49_31 PM" src="https://github.com/user-attachments/assets/aaa002df-2322-45ea-a355-4e24a775af60" />

**default=0** mencegah error saat mencari nomor terbesar dari data yang kosong.

Fungsi tambah_data(): menambah pegawai baru
Program meminta nama, profesi, dan unit kerja, lalu memeriksa:
- Apakah ada yang kosong? Kalau iya, ditolak.
- Apakah profesinya Dokter atau Perawat? Kalau bukan, ditolak.
Ada dua trik kecil di sini:
- profesi.lower() mengubah semua huruf jadi kecil. Jadi mau diketik "DOKTER", "Dokter", atau "dokter" tetap dianggap sama.
- max(data.keys(), default=0) + 1 mencari nomor terbesar yang sudah ada, lalu menambah 1 untuk nomor pegawai baru. Kalau data masih kosong, nomornya mulai dari 1.
Saat disimpan, capitalize() membuat huruf pertama jadi besar, jadi tampil rapi sebagai "Dokter".

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 8_50_27 PM" src="https://github.com/user-attachments/assets/86a4e0bf-c191-4896-b760-5ad38cb111a8" />

Fungsi ubah_data(): mengoreksi catatan
- Daftar data ditampilkan dulu supaya kamu bisa melihat nomornya.
- Memilih nomor yang mau diubah.
- Mengisi nama, profesi, dan unit kerja yang baru, dengan pengecekan yang sama seperti saat menambah.
- Catatan lama diganti dengan yang baru.
Ada juga pengaman try ... except ValueError. Artinya "coba jalankan ini, tapi kalau error karena yang diketik bukan angka, jangan sampai programnya mati". Program cukup menampilkan "Nomor harus berupa angka!"

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 8_50_45 PM" src="https://github.com/user-attachments/assets/194949a3-3e72-4e85-9e48-d156adef1c8d" />

**except ValueError** mencegah program mati kalau pengguna mengetik huruf padahal diminta angka.

Fungsi hapus_data(): membuang catatan
Caranya mirip ubah data: tampilkan daftar, pilih nomor, lalu cek apakah nomornya ada. Kalau ada, del data[nomor] menghapusnya.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 8_50_55 PM" src="https://github.com/user-attachments/assets/95e988a8-7653-4151-aa63-5f3f1f017cf6" />

Fungsi main(): pengatur jalannya program
- Login dulu. Program terus meminta login sampai berhasil (while True).
- Menu muncul berulang-ulang. Setiap kali kembali ke menu, layar dibersihkan dan ditampilkan judul, tanggal, serta role.
- Menu menyesuaikan role. Menu tambah, ubah, dan hapus hanya dicetak kalau role == "admin".
- Pilihan dicek satu per satu dengan if dan elif:
> 1 menampilkan data.
> 2, 3, 4 menjalankan fungsi masing-masing, tapi hanya kalau kamu admin.
> 0 menutup program.
> Selain itu muncul "Pilihan menu tidak valid!"
- Setelah selesai, program menunggu kamu menekan Enter supaya hasilnya sempat terbaca, lalu kembali ke menu.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 8_51_05 PM" src="https://github.com/user-attachments/assets/690d80d0-0008-4dda-b4bf-03325ec89a05" />

- Baris terakhir : Dari tadi semua fungsi hanya didefinisikan, belum dijalankan. Baris main() ini seperti menekan tombol "mulai", yang menjalankan seluruh program.

<img width="1366" height="705" alt="Flowchart_Pendataan_Dokter_Perawat_Revisi drawio - draw io 10_4_2026 8_40_18 PM" src="https://github.com/user-attachments/assets/aa9d635d-7a61-4c4d-b08e-80c6e516d5df" />

Flowchart Utama (login() dan main())
Langkah 1: Mulai
Hanya penanda awal program.

Langkah 2: Input username dan password
Program meminta dua isian: username = input(...) dan password = input(...).

Langkah 3: Keputusan "username ada di akun dan password cocok?"
Di kode: if username in akun and akun[username]["password"] == password.

Kalau benar (Ya):
- Program mencetak "Login berhasil!".
- Program mengembalikan username dan role (admin atau user).
- Perulangan login berhenti, lalu program lanjut ke menu.

Kalau salah (Tidak):
- Program mencetak "Username atau password salah!".
- Program mengembalikan None, None, sehingga username kosong.
- Karena username kosong, perulangan while True jalan lagi dan panah kembali ke atas ke input username.
- Tidak ada batas percobaan, jadi login bisa diulang tanpa batas.
Karena syaratnya memakai and, kalau username tidak ada di akun, password bahkan tidak dicek.

Langkah 4: Tampilkan menu
Layar dibersihkan, lalu tampil judul, tanggal hari ini, dan role. Menu 1 (Lihat Data) dan 0 (Keluar) selalu muncul. Menu 2, 3, dan 4 hanya dicetak kalau role == "admin".

Langkah 5: Input pilihan menu
Pilihan disimpan sebagai teks, misalnya "1", bukan angka. Itu sebabnya perbandingannya memakai tanda kutip.

Langkah 6: Belah ketupat "Pilihan menu?"
Di kode ini adalah rangkaian if / elif / else. Program mengecek dari atas ke bawah dan berhenti di syarat pertama yang benar.

Pilihan	Kalau syarat terpenuhi	Kalau tidak
"1"	Jalankan tampil_data(), tunggu Enter	Cek syarat berikutnya
"2" dan admin	Jalankan tambah_data(), tunggu Enter	Cek syarat berikutnya
"3" dan admin	Jalankan ubah_data(), tunggu Enter	Cek syarat berikutnya
"4" dan admin	Jalankan hapus_data(), tunggu Enter	Cek syarat berikutnya
"0"	Cetak "Program selesai.", berhenti	Masuk else
selain itu	Cetak "Pilihan menu tidak valid!", tunggu Enter	-

Kasus penting kalau role-nya user: user memilih "2". Syarat pilihan == "2" and role == "admin" salah karena role-nya bukan admin. Program lanjut ke syarat berikutnya, tidak ada yang cocok, lalu masuk else dan mencetak "Pilihan menu tidak valid!". Inilah kotak "Selain itu" di flowchart.

Langkah 7: Tekan Enter, lalu kembali ke menu
Setelah pilihan 1 sampai 4 atau pilihan tidak valid, program menunggu Enter supaya hasilnya sempat terbaca. Lalu panah panjang di sisi kiri membawa program kembali ke menu. Ini perulangan while True yang kedua.

Pilihan 0 berbeda: program langsung break tanpa menunggu Enter, lalu ke Selesai. Hanya cabang ini yang mengakhiri program.

**Flowchart Lihat Data (tampil_data)**
- Program mencetak judul "DATA DOKTER & PERAWAT".
- len(data) == 0?
> Benar (kosong): cetak "Belum ada data.", lalu selesai.
> Salah (ada isi): buat tabel dengan kolom No, Nama, Profesi, Unit Kerja. Program mengulang tiap isi data dan memasukkannya ke tabel dengan add_row, lalu mencetak tabel.

**Flowchart Tambah Data (tambah_data)**
- Program meminta nama, profesi, dan unit kerja.
- Ada yang kosong?
> Benar: cetak "Data tidak boleh kosong!", lalu return (fungsi berhenti).
> Salah: lanjut.
- profesi = profesi.lower() mengubah profesi jadi huruf kecil.
- Profesi bukan "dokter" dan bukan "perawat"?
> Benar: cetak "Profesi harus Dokter atau Perawat!", lalu return.
> Salah: lanjut.
- Nomor baru dihitung dengan max(data.keys(), default=0) + 1.
- Data disimpan dengan profesi.capitalize(), jadi tampil sebagai "Dokter" atau "Perawat".
- Program mencetak "Data berhasil ditambahkan.".
Di sini benar berarti ada masalah, karena pertanyaannya menanyakan kondisi yang salah.

**Flowchart Ubah Data (ubah_data)**
- Program memanggil tampil_data() supaya nomor yang tersedia terlihat.
- Program meminta nomor lewat int(input(...)).
- Input berupa angka?
> Benar: lanjut.
> Salah (misalnya mengetik "abc"): Python memunculkan ValueError, except menangkapnya, dan program mencetak "Nomor harus berupa angka!".
- Nomor ada di data?
> Benar: lanjut.
> Salah: cetak "Nomor data tidak ditemukan!", lalu return.
- Program meminta nama, profesi, dan unit kerja yang baru.
- Ada yang kosong? Kalau benar, cetak "Data tidak boleh kosong!", lalu return.
- lower(), lalu profesi tidak valid? Kalau benar, cetak "Profesi harus Dokter atau Perawat!", lalu return.
- Data lama ditimpa dengan data baru, lalu program mencetak "Data berhasil diubah.".

Pada langkah 3 dan 4, yang benar justru lanjut. Pada langkah 6 dan 7, yang benar berarti ada masalah. Itu karena arah pertanyaannya berbeda, jadi baca teks pertanyaannya dulu sebelum membaca label Ya atau Tidak.

**Flowchart Hapus Data (hapus_data)**
- Program memanggil tampil_data(), lalu meminta nomor yang mau dihapus.
- Input berupa angka?
> Salah: cetak "Nomor harus berupa angka!".
- Nomor ada di data?
> Benar: del data[nomor] menghapus data, lalu program mencetak "Data berhasil dihapus.".
> Salah: cetak "Nomor data tidak ditemukan!".

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 9_50_48 PM" src="https://github.com/user-attachments/assets/2109cb35-522b-4d2b-be33-1a3318424717" />

BERIKUT ADALAH HASIL OUTPUT ADMIN PADA NOMOR **1**.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 9_51_43 PM" src="https://github.com/user-attachments/assets/a35321ac-2446-4225-b312-0b63dd804273" />

BERIKUT ADALAH HASIL OUTPUT ADMIN PADA NOMOR **2**.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 9_53_47 PM" src="https://github.com/user-attachments/assets/136022be-48e2-4f5b-863e-4d328b3e27b4" />

BERIKUT ADALAH HASIL OUTPUT ADMIN PADA NOMOR **3**.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 9_54_03 PM" src="https://github.com/user-attachments/assets/f0f027dd-cc86-4229-b9bb-0612f9e505a1" />

BERIKUT ADALAH HASIL OUTPUT ADMIN PADA NOMOR **4**.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 9_54_12 PM" src="https://github.com/user-attachments/assets/3ee5c84c-52f1-4dc3-9298-12575e831ea0" />

BERIKUT ADALAH HASIL OUTPUT ADMIN PADA NOMOR **0** BEGITUPUN JUGA HASIL OUTPUT PADA USER.

<img width="1366" height="728" alt="MINI_PROJECT2_DDP py - Visual Studio Code 10_4_2026 9_54_51 PM" src="https://github.com/user-attachments/assets/c850ff6d-ca23-43a2-9ec3-74511720e661" />

BERIKUT ADALAH HASIL OUTPUT USER PADA NOMOR **1**.
