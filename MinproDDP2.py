import pwinput

akun = {
    "ATMIN": {"password": "ATMIN123", "role": "admin"},
    "USER1": {"password": "USER123", "role": "user"},
}

data_komik = []


def login():
    print("\nLOGIN")
    while True:
        username = input("Username: ").strip()
        password = pwinput.pwinput(prompt="Password: ", mask="*")
        if username in akun and akun[username]["password"] == password:
            return username, akun[username]["role"]
        print("Username atau password salah, coba lagi.")


def menu(role):
    print(f"\nMenu komik (Role: {role.upper()})")
    print("1. Tambah Data Komik")
    print("2. Tampilkan Data Komik")
    if role == "admin":
        print("3. Ubah Data Komik")
        print("4. Hapus Data Komik")
    print("5. Keluar")


def tambah_komik():
    judul = input("Masukkan Judul Komik: ").strip()
    genre = input("Masukkan Genre Komik: ").strip()
    chapter = input("Masukkan Jumlah Chapter: ").strip()
    if judul and genre and chapter.isdigit():
        data_komik.append({"judul": judul, "genre": genre, "chapter": int(chapter)})
        print("[Ok] Data komik berhasil ditambahkan.")
    else:
        print("[Gagal] Pastikan semua data terisi dan jumlah chapter berupa angka.")


def lihat_komik():
    if not data_komik:
        print("Belum ada data komik.")
        return
    print("\nDaftar Komik:")
    for i, k in enumerate(data_komik, start=1):
        print(f"{i}. {k['judul']} - {k['genre']} - {k['chapter']} chapter")


def ubah_komik():
    lihat_komik()
    nomor = input("Masukkan nomor komik yang ingin diubah: ").strip()
    if nomor.isdigit() and 1 <= int(nomor) <= len(data_komik):
        k = data_komik[int(nomor) - 1]
        judul = input(f"Judul baru [{k['judul']}]: ").strip()
        genre = input(f"Genre baru [{k['genre']}]: ").strip()
        chapter = input(f"Jumlah chapter baru [{k['chapter']}]: ").strip()
        if judul:
            k['judul'] = judul
        if genre:
            k['genre'] = genre
        if chapter.isdigit():
            k['chapter'] = int(chapter)
        print("[Ok] Data komik berhasil diubah.")
    else:
        print("Nomor komik tidak valid.")


def hapus_komik():
    lihat_komik()
    nomor = input("Masukkan nomor komik yang ingin dihapus: ").strip()
    if nomor.isdigit() and 1 <= int(nomor) <= len(data_komik):
        terhapus = data_komik.pop(int(nomor) - 1)
        print(f"[Ok] Komik '{terhapus['judul']}' berhasil dihapus.")
    else:
        print("Nomor komik tidak valid.")


def main():
    username, role = login()
    print(f"\nLogin berhasil sebagai {username} (Role: {role.upper()})")
    while True:
        menu(role)
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tambah_komik()
        elif pilihan == "2":
            lihat_komik()
        elif pilihan == "3" and role == "admin":
            ubah_komik()
        elif pilihan == "4" and role == "admin":
            hapus_komik()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()

