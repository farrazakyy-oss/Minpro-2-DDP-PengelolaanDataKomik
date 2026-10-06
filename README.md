# Minpro-2-DDP-PengelolaanDataKomik

(hasil meng-efisien-kan program mini project pertama)

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

jika cocok, functionnya return dua nilai: username dan role (dari akun[username]["role"], lalu looping otomatis berhenti jika fungsi selesai.

jika salah input, tampilkan pesan error dan while True mengulang dari awal.

<img width="466" height="157" alt="Screenshot 2026-10-06 230727" src="https://github.com/user-attachments/assets/a9bd9bc3-15f2-4f93-930d-b6fc56adbd1a" />

fungsi ini menerima parameter dari role, opsi tambah dan lihat selalu muncul untuk role apa saja, tapi baris 25  membuat opsi ubah dan hapus hanya muncul jika admin yang login.

<img width="732" height="177" alt="Screenshot 2026-10-06 230736" src="https://github.com/user-attachments/assets/85b917eb-76b4-472b-b504-a075b5076cb1" />

validasi input tidak kosong dan chapter harus angka, baru disimpan sebagai dictionary ke list

<img width="655" height="137" alt="Screenshot 2026-10-06 230745" src="https://github.com/user-attachments/assets/c9cb1e5d-c1ad-432f-9499-03bf620ae476" />

kode mengecek list yang kosong, lalu menampilkan semua data dengan nomor urut

<img width="657" height="333" alt="Screenshot 2026-10-06 230754" src="https://github.com/user-attachments/assets/02e77bb0-a3a3-4e7b-ac86-f129fabcc6cd" />

kode memvalidasi nomor data, lalu mengambil dictionarynya, dan mengupdate field yang diisi saja

<img width="615" height="157" alt="Screenshot 2026-10-06 230802" src="https://github.com/user-attachments/assets/ad5403b4-0913-4d57-867c-53a2a8dc644e" />

kode ini memvalidasi nomor data dan melakukan pop() dari list

<img width="632" height="452" alt="Screenshot 2026-10-06 230820" src="https://github.com/user-attachments/assets/d6589410-3c7f-42b8-9c20-747e7075af28" />

alur kode ini yaitu login dulu (menu loop), lalu mengarahkan ke function sesuai pilihan, dengan pengecekan role == admin untuk membatasi akses ubah/hapus.


# Output program

<img width="357" height="312" alt="Screenshot 2026-10-06 222826" src="https://github.com/user-attachments/assets/d0049451-0543-4c36-87d6-4d6dd5b316ee" />

ini adalah tampilan setelah menjalankan program dan login, serta output dari pilihan pertama

<img width="267" height="100" alt="Screenshot 2026-10-06 222842" src="https://github.com/user-attachments/assets/9357a902-1828-49e8-8f18-74251483f429" />

tampilan pilihan ke 2 untuk melihat data komik yang telah ditambahkan

<img width="345" height="185" alt="Screenshot 2026-10-06 222853" src="https://github.com/user-attachments/assets/ea5880fe-45ed-4005-b081-e3800c161ec5" />

tampilan pilihan ke 3 untuk mengubah data komik yang telah ditambahkan

<img width="350" height="132" alt="Screenshot 2026-10-06 222902" src="https://github.com/user-attachments/assets/ad1cb393-93c3-4045-b8e1-ef0c046f7576" />

tampilan pilihan ke 4 untuk menghapus data komik

<img width="358" height="65" alt="Screenshot 2026-10-06 222915" src="https://github.com/user-attachments/assets/b311ac88-24e8-4dba-8a62-9742992404a6" />

tampilan jika user memilih untuk berhenti (pilihan ke 5)
