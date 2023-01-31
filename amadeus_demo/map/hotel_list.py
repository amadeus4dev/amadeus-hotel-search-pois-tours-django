import geocoder 

class HotelList:

    def __init__(self, hotel_list):
        self.hotel_list = hotel_list

    def construct_hotel_list(self):
        try:
            list_offer = {}
            list_offer['name'] = self.hotel_list['name']
            list_offer['latitude'] = self.hotel_list['geoCode']['latitude']
            list_offer['longitude'] = self.hotel_list['geoCode']['longitude']
            address = geocoder.osm(
                [list_offer['latitude'], list_offer['longitude']], 
                method='reverse'
            )
            if address.json.get('houseNumber') is not None:
                list_offer['address'] = address.json['street'] + ' ' +  address.json['houseNumber']
            elif address.json.get('housenumber') is not None:
                list_offer['address'] = address.json['street'] + ' ' +  address.json['housenumber']
            else:
                list_offer['address'] = address.json['street']
                
        except (TypeError, AttributeError, KeyError):
            pass
        return list_offer
