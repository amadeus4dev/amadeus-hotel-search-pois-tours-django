class Hotel_list:
    def __init__(self, hotel_list):
        self.hotel_list = hotel_list

    def construct_hotel_list(self):
        try:
            list_offer = {}
            list_offer['name'] = self.hotel_list['name']
            list_offer['latitude'] = self.hotel_list['geoCode']['latitude']
            list_offer['longitude'] = self.hotel_list['geoCode']['longitude']
            # offer['address'] = self.hotel_list['address']
        except (TypeError, AttributeError, KeyError):
            pass
        return list_offer
