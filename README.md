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