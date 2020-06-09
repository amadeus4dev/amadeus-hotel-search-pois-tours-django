import os
import json
import requests
from amadeus import Client, ResponseError
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .hotel import Hotel
from .point_of_interest import PointOfInterest
from .safety import Safety

amadeus = Client()


def hotels_map(request):
    hotels = search_hotels('SFO')
    HERE_API_KEY = os.environ.get('HERE_API_KEY')
    return render(request, 'map/map.html', {'hotels': json.dumps(hotels),
                                            'here_api_key': HERE_API_KEY
                                            })


def search_hotels(city_code):
    hotels = amadeus.shopping.hotel_offers.get(cityCode=city_code,
                                               includeClosed='true')
    hotel_offers = []
    for hotel in hotels.data:
        print(hotel)
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


@csrf_exempt
def search_safety(request):
    if request.is_ajax():
            try:
                safety_returned = []
                safety = amadeus.get('/v1/safety/safety-rated-locations',
                    latitude=request.POST.get('hotel_lat'),
                    longitude=request.POST.get('hotel_lng')).data
                safety_returned.append(Safety(safety).construct_safety_scores())
            except ResponseError as error:
                messages.add_message(request, messages.ERROR, error)
    return HttpResponse(json.dumps(safety_returned))
