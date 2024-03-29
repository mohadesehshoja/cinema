from django.contrib import admin
from django.urls import path
from tickting.views import movie_list, cinema_list
from account import views
urlpatterns=[
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path("profile/details",views.profile_details,name='profile_details'),
    path("payment/list",views.payment_list,name='payment_list'),
    path("payment/creat",views.payment_creat,name='payment_creat'),
    path("profile/edit",views.profile_edit,name='profile_edit'),
    path("password/change",views.change_password,name='password_change'),
]