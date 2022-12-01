from amadeus import ResponseError, Client

amadeus = Client(
    client_id='Y0v5D4pbkijUvoNjLozwzJqTph8lr4CR',
    client_secret='5544MxgSurVZIOtx'
)

try:
    '''
    Returns safety information for a location in Barcelona based on geolocation coordinates
    '''
    response = amadeus.safety.safety_rated_locations.get(latitude=41.397158, longitude=2.160873, radius=2)
    print(response.data)
except ResponseError as error:
    raise error