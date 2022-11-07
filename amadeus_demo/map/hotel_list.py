class Hotel_list:
    def __init__(self, hotel_list):
        self.hotel_list = hotel_list

    def construct_hotel_list(self):
        try:
            offer = {}
            offer['name'] = self.hotel_list['name']
            offer['latitude'] = self.hotel_list['geoCode']['latitude']
            offer['longitude'] = self.hotel_list['geoCode']['longitude']
            offer['address'] = self.hotel_list['address']
        except (TypeError, AttributeError, KeyError):
            pass
        return offer
