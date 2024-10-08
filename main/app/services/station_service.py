class StationService:
    def __init__(self, charging_stations):
        self.charging_stations = charging_stations
    
    def get_stations(self, page, size):
        stations = self.charging_stations.find_all(page, size)
        return [self.charging_stations.to_dict(station) for station in stations]
    
    def get_nearest_station(self, latitude, longitude, threshold):
        stations = self.charging_stations.find_nearest(latitude, longitude, threshold)
        return stations
