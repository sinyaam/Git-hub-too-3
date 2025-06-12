from feature_europe_asia import MurderStatsManager

class ExtendedMurderStatsManager(MurderStatsManager):

    def get_city_stats(self, continent, country, city):
        if continent in self.data:
            if country in self.data[continent]:
                if city in self.data[continent][country]:
                    return self.data[continent][country][city]


    def remove_city(self, continent, country, city):
        if continent in self.data:
            if country in self.data[continent]:
                if city in self.data[continent][country]:
                    del self.data[continent][country][city]
                    print(f"{city} удалён.")
   

stats_manager = MurderStatsManager()
stats_manager.data = {
    "Europe": {
        "Estonia": {
            "Tallinn": 5
        },
        "Finland": {
            "Helsinki": 3
        }
    },
    "Asia": {
        "Japan": {
            "Tokyo": 8
        }
    }
}


print("Текущие данные:")
stats_manager.get_stats()


stats_manager.add_data("Europe", "Finland", "Helsinki", 4)
print("\nПосле обновления данных (Helsinki -> 4):")
stats_manager.get_stats()


print("\nТестирование ExtendedMurderStatsManager:")
extended_stats_manager = ExtendedMurderStatsManager()
extended_stats_manager.data = {
    "Europe": {
        "Estonia": {
            "Tallinn": 5
        },
        "Finland": {
            "Helsinki": 3
        }
    },
    "Asia": {
        "Japan": {
            "Tokyo": 8
        }
    },
    "Africa": {
        "Nigeria": {
            "Lagos": 7
        },
        "South Africa": {
            "Johannesburg": 6
        },
        "Egypt": {
            "Cairo": 4
        }
    }
}


print("Текущие данные:")
extended_stats_manager.get_stats()


city_stats = extended_stats_manager.get_city_stats("Africa", "Egypt", "Cairo")
print(f"\nСтатистика для города Cairo: {city_stats}")


extended_stats_manager.remove_city("Africa", "Egypt", "Cairo")
print("\nПосле удаления города Cairo:")
extended_stats_manager.get_stats()