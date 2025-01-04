import json
import os
from data.weather_data import WeatherData
from view.weather_view import WeatherView

class WeatherProcess:
    def __init__(self, data_file="weather_data.json"):
        self.data_list = []
        self.data_file = data_file
        self.load_data()  # Memuat data dari file saat program dimulai

    def add_weather(self):
        city = input("Masukkan nama kota: ").strip()
        condition = input("Masukkan ramalan cuaca (cerah/hujan/mendung): ").strip().lower()

        # Validasi input
        if not city or condition not in ["cerah", "hujan", "mendung"]:
            print("Input tidak valid. Silakan coba lagi.")
            return

        # Menambah data ke list
        self.data_list.append(WeatherData(city, condition))
        print(f"Data ramalan cuaca untuk kota {city} berhasil ditambahkan!")

        # Simpan data ke file JSON
        self.save_data()

    def show_weather(self):
        WeatherView.display_weather(self.data_list)

    def save_data(self):
        """Menyimpan data_list ke file JSON."""
        try:
            with open(self.data_file, "w") as file:
                json_data = [{"city": data.city, "condition": data.condition} for data in self.data_list]
                json.dump(json_data, file, indent=4)
            print("Data berhasil disimpan!")
        except Exception as e:
            print(f"Terjadi kesalahan saat menyimpan data: {e}")

    def load_data(self):
        """Memuat data dari file JSON ke dalam data_list."""
        if not os.path.exists(self.data_file):
            return  # Jika file belum ada, abaikan

        try:
            with open(self.data_file, "r") as file:
                json_data = json.load(file)
                self.data_list = [WeatherData(item["city"], item["condition"]) for item in json_data]
            print("Data berhasil dimuat!")
        except Exception as e:
            print(f"Terjadi kesalahan saat memuat data: {e}")
