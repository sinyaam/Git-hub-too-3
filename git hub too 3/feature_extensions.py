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
stats2 =    
data = {
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

    