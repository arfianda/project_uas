# Program Ramalan Cuaca Sederhana 🌤️

## Deskripsi Singkat
Program **Ramalan Cuaca Sederhana** ini dibuat menggunakan bahasa Python dengan konsep **Object-Oriented Programming (OOP)** dan pembagian modular ke dalam beberapa folder. Program ini memungkinkan pengguna untuk:
- Menambah data ramalan cuaca untuk kota tertentu.
- Menampilkan daftar ramalan cuaca dalam bentuk tabel.
- Menyimpan data ke dalam file JSON, sehingga data tetap tersimpan meskipun program dihentikan.
- Memuat data dari file JSON ketika program dijalankan kembali.

Program ini dibuat untuk UAS matakuliah Bahasa Pemrograman Universitas Pelita Bangsa Teknik Informatika.
## Struktur Folder
```plaintext
WeatherApp/
├── data/               # Mengelola struktur data
│   ├── __init__.py
│   ├── weather_data.py
├── view/               # Menampilkan data ke pengguna
│   ├── __init__.py
│   ├── weather_view.py
├── process/            # Proses bisnis aplikasi
│   ├── __init__.py
│   ├── weather_process.py
├── main.py             # File utama untuk menjalankan program
├── requirements.txt    # Dependensi library yang digunakan
```

## Fitur Utama

1. Tambah Data Ramalan Cuaca: Input nama kota dan kondisi cuaca (cerah, hujan, mendung).

2. Tampilkan Data: Menampilkan data ramalan cuaca dalam bentuk tabel menggunakan library `tabulate`.

3. Simpan Data: Data otomatis disimpan ke file `JSON` saat program keluar.

4. Muat Data: Data otomatis dimuat dari file `JSON` saat program dijalankan kembali.


## Cara Menjalankan Program

1. Clone repository ini ke komputer Anda.

2. Pastikan Python sudah terinstal.
3. Install library yang dibutuhkan:
```bash
pip install -r requirements.txt
```
4. Jalankan program dengan perintah:
```bash
python main.py
```
5. Ikuti instruksi yang muncul di layar untuk menggunakan program.

## Link Video Penjelasan





