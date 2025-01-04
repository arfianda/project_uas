from tabulate import tabulate

class WeatherView:
    @staticmethod
    def display_weather(data_list):
        if not data_list:
            print("Belum ada data ramalan cuaca.")
            return
        table = [[i+1, data.city, data.condition] for i, data in enumerate(data_list)]
        headers = ["No", "Kota", "Ramalan Cuaca"]
        print(tabulate(table, headers, tablefmt="grid"))
