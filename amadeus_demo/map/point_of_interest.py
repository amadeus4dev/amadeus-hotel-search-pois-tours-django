class PointOfInterest:
    def __init__(self, poi):
        self.poi = poi

    def construct_poi(self):
        try:
            place = {}
            place['name'] = self.poi['name']
        except (TypeError, AttributeError, KeyError):
            pass
        return place