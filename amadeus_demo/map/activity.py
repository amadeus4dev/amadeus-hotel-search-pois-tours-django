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
            activity_returned['price'] = self.activity['price']['amount']
            activity_returned['currency'] = self.activity['price']['currencyCode']
        except (TypeError, AttributeError, KeyError):
            pass
        return activity_returned

    def format_rating(self, rating):
        return "{0:0.1f}".format(float(rating))
