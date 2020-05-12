class PointOfInterest:
    
    def __init__(self, poi):
        self.poi = poi

    def construct_poi(self):
        try:
            place = {}
            place['name'] = self.poi['name']
            place['category'] = self.poi['category']
            place['lat'] = self.poi['geoCode']['latitude']
            place['lng'] = self.poi['geoCode']['longitude']
        except (TypeError, AttributeError, KeyError):
            pass
        return place