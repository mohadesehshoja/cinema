from django.contrib import admin
from django.urls import path
from tickting.views import movie_list, cinema_list
from tickting import views
urlpatterns = [
    path('movie/list',views.movie_list,name='movie_list'),
    path('movie/details/<int:movie_id>/',views.movie_details,name='movie_details'),
    path('cinema/list',views.cinema_list,name='cinema-list'),
    path('cinema/details/<int:cinema_id>/',views.cinema_details,name='cinema_details'),
    path('showtime/list',views.showtime_list,name='showtime_list'),
    path('ticket/list',views.ticket_list,name='ticket_list'),
    path('ticket/details/<int:ticket_id>/',views.ticket_details,name='ticket_details'),
    path('showtime/details/<int:showtime_id>',views.showtime_details,name="showtime_details")
]
