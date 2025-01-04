from process.weather_process import WeatherProcess

def main():
    print("=== Program Ramalan Cuaca Sederhana ===")
    process = WeatherProcess()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Ramalan Cuaca")
        print("2. Tampilkan Ramalan Cuaca")
        print("3. Keluar")
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            process.add_weather()
        elif choice == "2":
            process.show_weather()
        elif choice == "3":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
