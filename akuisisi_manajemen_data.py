# Tugas 1 - Akuisisi dan Manajemen Data
# Jalankan kode ini dari atas ke bawah.

# 1. Memeriksa environment Python
import sys
import platform
import importlib.util

print("Versi Python:", sys.version)
print("Sistem Operasi:", platform.platform())

# 2. Memeriksa library yang diperlukan
packages = {
    "pandas": "pandas",
    "numpy": "numpy",
    "requests": "requests",
    "beautifulsoup4": "bs4"
}

for nama, modul in packages.items():
    if importlib.util.find_spec(modul):
        print(nama, "sudah terpasang")
    else:
        print(nama, "belum terpasang")

# Jika ada library yang belum terpasang, jalankan perintah ini
# di terminal: pip install pandas numpy requests beautifulsoup4

# 3. Membuat struktur folder proyek
from pathlib import Path

folders = [
    "data/raw",
    "data/interim",
    "data/processed",
    "notebooks",
    "src",
    "docs",
    "reports"
]

for folder in folders:
    path = Path(folder)
    path.mkdir(parents=True, exist_ok=True)
    (path / ".gitkeep").touch(exist_ok=True)
    print("Folder dibuat:", folder)

# 4. Membuat README.md
readme = """# Akuisisi dan Manajemen Data

## Identitas
Nama: ISI NAMA ANDA
NIM: ISI NIM ANDA
Mata Kuliah: Akuisisi dan Manajemen Data

## Tujuan
Memahami tahapan data lifecycle dan menyiapkan environment
untuk proyek akuisisi dan manajemen data.

## Struktur Folder
- data/raw: data mentah, tidak diubah
- data/interim: data sementara
- data/processed: data hasil pembersihan
- notebooks: notebook analisis
- src: kode program
- docs: dokumentasi
- reports: laporan hasil

## Cara Menjalankan
1. Gunakan Python 3.11 atau versi yang lebih baru.
2. Pasang pandas, numpy, requests, dan beautifulsoup4.
3. Jalankan kode dari bagian pertama sampai terakhir.
4. Periksa hasil tabel lifecycle dan dokumentasi.
"""

Path("README.md").write_text(readme, encoding="utf-8")
print("README.md berhasil dibuat")

# 5. Membuat tabel Data Lifecycle
import pandas as pd

lifecycle = [
    {
        "Tahap": "Acquisition",
        "Aktivitas": "Mengumpulkan data dari sumber",
        "Tools": "requests, BeautifulSoup",
        "Risiko": "Data salah, tidak lengkap, atau sumber tidak tepercaya",
        "Output": "Data mentah"
    },
    {
        "Tahap": "Storage",
        "Aktivitas": "Menyimpan data secara terstruktur",
        "Tools": "CSV, PostgreSQL",
        "Risiko": "Data hilang, rusak, atau akses tidak sah",
        "Output": "Data tersimpan"
    },
    {
        "Tahap": "Cleaning",
        "Aktivitas": "Menangani data kosong, duplikat, dan kesalahan",
        "Tools": "pandas, OpenRefine",
        "Risiko": "Data penting terhapus atau kesalahan tidak diperbaiki",
        "Output": "Data bersih"
    },
    {
        "Tahap": "Transformation",
        "Aktivitas": "Mengubah format dan struktur data",
        "Tools": "pandas, NumPy",
        "Risiko": "Perubahan format atau perhitungan keliru",
        "Output": "Data tertransformasi"
    },
    {
        "Tahap": "Analysis",
        "Aktivitas": "Menganalisis pola dan informasi dari data",
        "Tools": "pandas, Matplotlib",
        "Risiko": "Kesimpulan bias atau salah",
        "Output": "Hasil analisis"
    },
    {
        "Tahap": "Delivery",
        "Aktivitas": "Menyampaikan hasil analisis",
        "Tools": "Jupyter Notebook, Power BI",
        "Risiko": "Informasi salah disampaikan atau data sensitif bocor",
        "Output": "Laporan atau visualisasi"
    }
]

df = pd.DataFrame(lifecycle)
print(df.to_string(index=False))

# 6. Menyimpan tabel sebagai CSV dan Excel
df.to_csv("data_lifecycle.csv", index=False, encoding="utf-8")
df.to_excel("data_lifecycle.xlsx", index=False)
print("Tabel berhasil disimpan ke CSV dan Excel")

# 7. Paragraf reproduksibilitas
paragraf = """
Reproducibility atau reproduksibilitas adalah kemampuan untuk
mengulangi proses pengolahan dan analisis data sehingga
menghasilkan hasil yang konsisten dengan menggunakan data,
kode, dan langkah kerja yang sama. Reproduksibilitas penting
dalam data science karena membantu peneliti memeriksa kebenaran
hasil, menemukan kesalahan, dan memastikan bahwa kesimpulan
tidak hanya bergantung pada satu kali percobaan. Dokumentasi
yang jelas, pencatatan versi library, penyimpanan data yang
terstruktur, serta penggunaan Git dapat membantu menjaga
reproduksibilitas sebuah proyek.

Contoh kasus adalah analisis data penjualan sebuah toko.
Seorang analis mengumpulkan data transaksi, membersihkan data
kosong, menghapus duplikasi, kemudian menghitung total
penjualan setiap bulan. Jika seluruh langkah tersebut dicatat
dalam notebook dan kode disimpan menggunakan Git, analis lain
dapat menjalankan kembali proses yang sama untuk memeriksa
hasilnya. Apabila hasil berbeda, mereka dapat memeriksa perubahan
data, kode, atau versi library yang digunakan. Dengan demikian,
reproduksibilitas meningkatkan transparansi, mempermudah kerja
sama, dan membantu pengambilan keputusan berdasarkan hasil
analisis yang dapat diperiksa kembali.
"""

jumlah_kata = len(paragraf.split())
print("\nParagraf reproduksibilitas:")
print(paragraf)
print("Jumlah kata:", jumlah_kata)

if not 150 <= jumlah_kata <= 200:
    print("Catatan: sesuaikan paragraf agar jumlah kata 150-200.")

# 8. Pemeriksaan hasil proyek
print("\n=== PEMERIKSAAN PROYEK ===")
for nama_file in ["README.md", "data_lifecycle.csv", "data_lifecycle.xlsx"]:
    print(nama_file, "BERHASIL" if Path(nama_file).exists() else "BELUM TERSEDIA")

print("\n=== PEMERIKSAAN FOLDER ===")
for folder in folders:
    print(folder, "BERHASIL" if Path(folder).is_dir() else "BELUM TERSEDIA")

# Catatan Git:
# Jalankan perintah berikut di terminal, bukan di sel Python:
# git init
# git add .
# git commit -m "Tugas 1 Akuisisi dan Manajemen Data"
# git branch -M main
# git remote add origin URL_REPOSITORY_GITHUB_KAMU
# git push -u origin main
