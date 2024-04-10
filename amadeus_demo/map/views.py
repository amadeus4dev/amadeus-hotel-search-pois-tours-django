import os
import json
from amadeus import Client, ResponseError
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .hotel_list import HotelList
from .point_of_interest import PointOfInterest
from .activity import Activity

amadeus = Client()

def hotels_map(request):
    hotels = search_hotels('BCN')
    HERE_API_KEY = os.environ.get('HERE_API_KEY')
    return render(request, 'map/map.html', {'hotels': json.dumps(hotels),
                                            'here_api_key': HERE_API_KEY
                                            })


def search_hotels(city_code):
    hotels = amadeus.reference_data.locations.hotels.by_city.get(cityCode=city_code)
    hotel_offers = []
    for hotel in hotels.data[:15]:
        list_offer = HotelList(hotel).construct_hotel_list()
        hotel_offers.append(list_offer)
    return hotel_offers


@csrf_exempt
def search_pois(request):
    points_of_interest = []
    if request.is_ajax():
        try:
            pois = amadeus.reference_data.locations.points_of_interest.get(
                latitude=request.POST.get('lat'),
                longitude=request.POST.get('lng'),
                radius=2)
            points_of_interest = []
            for p in pois.data:
                poi = PointOfInterest(p).construct_poi()
                points_of_interest.append(poi)
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
    return HttpResponse(json.dumps(points_of_interest))


@csrf_exempt
def search_activity(request):
    if request.is_ajax():
        try:
            activities = amadeus.shopping.activities.get(
                latitude=request.POST.get('lat'),
                longitude=request.POST.get('lng'),
                radius=2)
            activities_returned = []
            for a in activities.data:
                activity = Activity(a).construct_activity()
                activities_returned.append(activity)
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
    return HttpResponse(json.dumps(activities_returned))
