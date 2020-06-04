class Hotel:
    def __init__(self, hotel):
        self.hotel = hotel

    def construct_hotel(self):
        try:
            offer = {}
            offer['name'] = self.hotel['hotel']['name']
            offer['latitude'] = self.hotel['hotel']['latitude']
            offer['longitude'] = self.hotel['hotel']['longitude']
            offer['address'] = self.hotel['hotel']['address']['lines']
        except (TypeError, AttributeError, KeyError):
            pass
        return offer
