# Minpro-2-DDP-PengelolaanDataKomik

## Penjelasan Singkat Program
program ini adalah sistem CRUD data komik (judul, genre, jumlah chapter) yang hanya bisa diakses setelah login.

alur program: login dengan memasukkan username dan password, yang dicek lewat dictionary akun, passwordnya disembunyikan dengan pwinput.

ada 2 role: admin dan user biasa, admin bisa tambah, lihat, ubah dan hapus data, sedangkan user biasa hanya bisa tambah dan lihat data.

datanya disimpan di list data_komik, setiap komik itu berupa dictionary

lalu menu program juga berulang (while True) sampai user memilih 5/keluar

## Penjelasan Kode

<img width="497" height="157" alt="Screenshot 2026-10-06 224755" src="https://github.com/user-attachments/assets/56a52aa7-eb27-491b-88a7-07eeab243e25" />

import pwinput untuk mengimpor library pwinput agar bisa dipakai,

lalu akun dan isinya sebagai dictionary bersarang sebagai database

data_komik sebagai list kosong untuk menyimpan data komik.

<img width="632" height="160" alt="Screenshot 2026-10-06 224805" src="https://github.com/user-attachments/assets/2f69a9a8-bcca-4342-a5ea-081601e38514" />

while true disini membuat looping yang dimana user harus login hingga berhasil

baris 14 mengambil input username biasa

baris 15 mengambil input password lewat pwinput, jadi yang diketik akan muncul sebagai *

baris 16 adalah conditional statement yang mengecek apakah username ada sebagai key di dictionary dan apakah password yang dimasukkan cocok dengan akun[username]["password"]

jika cocok, functionnya return dua nilai
