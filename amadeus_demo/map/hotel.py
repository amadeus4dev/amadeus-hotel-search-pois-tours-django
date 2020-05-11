class Hotel:
    def __init__(self, hotel):
        self.hotel = hotel

    def construct_hotel(self):
        try:
            offer = {}
            offer['price'] = self.hotel['offers'][0]['price']['total']
            offer['name'] = self.hotel['hotel']['name']
            offer['latitude'] = self.hotel['hotel']['latitude']
            offer['longitude'] = self.hotel['hotel']['longitude']
            offer['hotelID'] = self.hotel['hotel']['hotelId']
            offer['distance'] = self.hotel['hotel']['hotelDistance']['distance']
            offer['description'] = self.hotel['hotel']['description']['text']
            offer['address'] = self.hotel['hotel']['address']['lines']
        except (TypeError, AttributeError, KeyError):
            pass
        return offer