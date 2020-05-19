from django.shortcuts import render
from amadeus import Client, ResponseError, Location
from .hotel import Hotel
from .point_of_interest import PointOfInterest
import json
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

amadeus = Client()


def hotels_map(request):
    hotels = search_hotels('BCN')
    return render(request, 'map/map.html', {'hotels': json.dumps(hotels)})


def search_hotels(city_code):
    hotels = amadeus.shopping.hotel_offers.get(latitude='41.397158', longitude='2.160873')
    hotel_offers = []
    for hotel in hotels.data:
        offer = Hotel(hotel).construct_hotel()
        hotel_offers.append(offer)
    return hotel_offers


@csrf_exempt
def search_pois(request):
    if request.is_ajax():
        try:
            pois = amadeus.reference_data.locations.points_of_interest.get(
                latitude=request.POST.get('lat'), 
                longitude=request.POST.get('lng'))
            points_of_interest = []
            for p in pois.data:
                poi = PointOfInterest(p).construct_poi()
                points_of_interest.append(poi)
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
    return HttpResponse(json.dumps(points_of_interest))