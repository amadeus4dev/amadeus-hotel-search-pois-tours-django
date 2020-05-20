import os
import requests

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
            offer['safety'] = self.safety(offer['latitude'], offer['longitude'])
                   
        except (TypeError, AttributeError, KeyError):
            pass
        return offer
    
    def safety(self, lat, lng):
        GEOSURE_ACCESS_TOKEN = os.environ.get('GEOSURE_ACCESS_TOKEN')
        GEOSURE_ENDPOINT = os.environ.get('GEOSURE_ENDPOINT')
        parameters = {"latitude":lat,
                    "longitude": lng,
                    "access_token": GEOSURE_ACCESS_TOKEN
                    }

        safety = requests.get(url= GEOSURE_ENDPOINT,
                            params=parameters).json() 
        overall = safety['data'][0]['safetyScores']['overall']    
        lgbtq   = safety['data'][0]['safetyScores']['lgbtq']   
        theft   = safety['data'][0]['safetyScores']['theft']     
        medical = safety['data'][0]['safetyScores']['medical']                           
        return f'overall safety: {overall}\nlgbtq: {lgbtq}\ntheft: {theft}\nmedical: {medical}'
