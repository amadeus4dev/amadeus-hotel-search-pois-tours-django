class Activity:

    def __init__(self, activity):
        self.activity = activity

    def construct_activity(self):
        try:
            activity_returned = {}
            activity_returned['name'] = self.activity['name']
            activity_returned['rating'] = self.format_rating(self.activity['rating'])
            activity_returned['link'] = self.activity['bookingLink']
            activity_returned['lat'] = self.activity['geoCode']['latitude']
            activity_returned['lng'] = self.activity['geoCode']['longitude']
        except (TypeError, AttributeError, KeyError):
            pass
        return activity_returned

    def classify_poi_rank(self, rank):
        if rank <= 30:
            return f'<div>Top {rank} &#129351</div>'
        elif 30 < rank <= 50:
            return f'<div>Top {rank} &#129352</div>'
        elif 50 < rank <= 100:
            return f'<div>Top {rank} &#129353</div>'
        else:
            return f'<div>Top {rank}</div>'

    def format_rating(self, rating):
        return "{0:0.1f}".format(float(rating))

