from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotels_map, name='hotels_map'),
    path('search_pois/', views.search_pois, name='search_pois'),
    path('search_safety/', views.search_safety, name='search_safety'),
    path('search_activity/', views.search_activity, name='search_activity'),

]
