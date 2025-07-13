import json
from abc import ABC, abstractmethod

# ==================== Abstract & Polymorphic Class ====================
class DailyActivity(ABC):
    def __init__(self, tanggal, deskripsi):
        self.tanggal = tanggal
        self.deskripsi = deskripsi

    @abstractmethod
    def tampilkan_kegiatan(self):
        pass

# ==================== Subclasses ====================
class TrainingActivity(DailyActivity):
    def tampilkan_kegiatan(self):
        return f"[LATIHAN] {self.tanggal} - {self.deskripsi}"

class WatchingMatchActivity(DailyActivity):
    def tampilkan_kegiatan(self):
        return f"[NONTON MATCH] {self.tanggal} - {self.deskripsi}"

class ContentCreationActivity(DailyActivity):
    def tampilkan_kegiatan(self):
        return f"[BUAT KONTEN] {self.tanggal} - {self.deskripsi}"

# ==================== Match Review ====================
class MatchReview:
    def __init__(self, tanggal, tim1, tim2, skor, pemain_terbaik):
        self.tanggal = tanggal
        self.tim1 = tim1
        self.tim2 = tim2
        self.skor = skor
        self.pemain_terbaik = pemain_terbaik

    def ringkasan_match(self):
        return f"{self.tanggal} | {self.tim1} {self.skor} {self.tim2} | Pemain Terbaik: {self.pemain_terbaik}"

# ==================== Content Idea ====================
class ContentIdea:
    def __init__(self, judul, platform, tanggal_upload, status):
        self.judul = judul
        self.platform = platform
        self.tanggal_upload = tanggal_upload
        self.status = status

    def tampilkan_ide(self):
        return f"[Konten] {self.judul} | {self.platform} | Upload: {self.tanggal_upload} | Status: {self.status}"

# ==================== In-Memory Storage ====================
data_storage = {
    "activities": [],
    "match_reviews": [],
    "content_ideas": []
}

# ==================== CLI Menu ====================
def menu():
    while True:
        print("\n--- SoccerLife Tracker ---")
        print("1. Tambah Kegiatan Harian")
        print("2. Tulis Review Pertandingan")
        print("3. Tambah Ide Konten")
        print("4. Lihat Semua Data")
        print("5. Keluar")
        try:
            pilihan = input("Pilih menu: ")
        except (EOFError, OSError):
            print("\nTerjadi kesalahan input. Keluar dari program.")
            break

        if pilihan == "1":
            tambah_kegiatan()
        elif pilihan == "2":
            tambah_review()
        elif pilihan == "3":
            tambah_konten()
        elif pilihan == "4":
            tampilkan_data()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid")

# ==================== Menu Functions ====================
def tambah_kegiatan():
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    jenis = input("Jenis (latihan/nonton/konten): ").lower()
    deskripsi = input("Deskripsi: ")

    if jenis == "latihan":
        aktivitas = TrainingActivity(tanggal, deskripsi)
    elif jenis == "nonton":
        aktivitas = WatchingMatchActivity(tanggal, deskripsi)
    elif jenis == "konten":
        aktivitas = ContentCreationActivity(tanggal, deskripsi)
    else:
        print("Jenis tidak valid")
        return

    data_storage["activities"].append({"kegiatan": aktivitas.tampilkan_kegiatan()})
    print("Kegiatan berhasil ditambahkan!")

def tambah_review():
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    tim1 = input("Tim 1: ")
    tim2 = input("Tim 2: ")
    skor = input("Skor (cth: 2-1): ")
    pemain_terbaik = input("Pemain Terbaik: ")

    review = MatchReview(tanggal, tim1, tim2, skor, pemain_terbaik)
    data_storage["match_reviews"].append({"review": review.ringkasan_match()})
    print("Review berhasil disimpan!")

def tambah_konten():
    judul = input("Judul Konten: ")
    platform = input("Platform (Instagram/YouTube/TikTok): ")
    tanggal_upload = input("Tanggal Upload (YYYY-MM-DD): ")
    status = input("Status (draft/sudah upload): ")

    ide = ContentIdea(judul, platform, tanggal_upload, status)
    data_storage["content_ideas"].append({"konten": ide.tampilkan_ide()})
    print("Ide konten ditambahkan!")

def tampilkan_data():
    print("\n--- Semua Kegiatan Harian ---")
    for item in data_storage["activities"]:
        print("-", item["kegiatan"])

    print("\n--- Semua Review Pertandingan ---")
    for item in data_storage["match_reviews"]:
        print("-", item["review"])

    print("\n--- Semua Ide Konten ---")
    for item in data_storage["content_ideas"]:
        print("-", item["konten"])

# ==================== Run Program ====================
if __name__ == "__main__":
    menu()

