class PointOfInterest:
    
    def __init__(self, poi):
        self.poi = poi

    def construct_poi(self):
        try:
            place = {}
            place['name'] = self.poi['name']
            place['category'] = self.poi['category']
            place['rank'] = self.classify_poi_rank(self.poi['rank'])
            place['lat'] = self.poi['geoCode']['latitude']
            place['lng'] = self.poi['geoCode']['longitude']
        except (TypeError, AttributeError, KeyError):
            pass
        return place

    def classify_poi_rank(self, rank):
        if rank <= 30:
            return f'<div>Top {rank} &#129351</div>'
        elif 30 < rank <= 50:
            return f'<div>Top {rank} &#129352</div>'
        elif 50 < rank <= 100:
            return f'<div>Top {rank} &#129353</div>'
        else:
            return f'<div>Top {rank}</div>'
