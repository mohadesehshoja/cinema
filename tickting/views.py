from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import django.shortcuts

from tickting.forms import showtimesearch
from tickting.models import Movie, Cinema, Showtime, Ticket
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def movie_list(request):
    #1-selected deta
    movies=Movie.objects.all()
    count=Movie.objects.count()
    context={
        'movies_list':movies,
        'count':count
    }
    #render response
    return render(request,'movie_list.html',context)
def cinema_list(request):
    cinemas=Cinema.objects.all()
    context={
        'cinema_list':cinemas
    }
    return render(request,'cinema_list.html',context)
def movie_details(request,movie_id):
    movie=get_object_or_404(Movie,pk=movie_id)
    context={
        'movie':movie
    }
    return render(request,"movie_details.html",context)
def cinema_details(request,cinema_id):
    cinema=get_object_or_404(Cinema,pk=cinema_id)
    context={
        'cinema':cinema
    }
    return render(request,"cinema_details.html",context)

def showtime_list(request):
    var = request.user.is_authenticated
    searchform=showtimesearch(request.GET)
    showtimes = Showtime.objects.all()
    if searchform.is_valid():
        showtimes=showtimes.filter(movie__name__contains=searchform.cleaned_data['movie_name'])
        if searchform.cleaned_data['sale_is_open']:
            showtimes=showtimes.filter(status=Showtime.SALE_OPEN)
        if searchform.cleaned_data['movie_length_min'] is not None:
            showtimes=showtimes.filter(movie__length__gte=searchform.cleaned_data['movie_length_min'])
        if searchform.cleaned_data['movie_length_max'] is not None:
            showtimes=showtimes.filter(movie__length__lte=searchform.cleaned_data['movie_length_max'])
        if searchform.cleaned_data['cinema_filter'] is not None:
            showtimes=showtimes.filter(cinema=searchform.cleaned_data['cinema_filter'])
        minprice , maxprice = searchform.get_price_level()
        if minprice is not None:
            showtimes=showtimes.filter(price__gte=minprice)
        if maxprice is not None:
            showtimes=showtimes.filter(price__lt=maxprice)
    showtimes=showtimes.order_by('start_time')
    context={
        'showtimes':showtimes,
        'searchfrom':searchform
    }
    if var==True:
        return render(request, 'showtime_list.html', context)
    else:
        return HttpResponseRedirect(reverse("login")+ "?next=/tickting/showtime/list")
@login_required
def ticket_list(request):
    tickets=Ticket.objects.filter(customer=request.user.profile).order_by("-order_time")
    context={
        'tickets':tickets
    }
    return render(request,'ticket_list.html',context)
@login_required
def ticket_details(request,ticket_id):
    ticket=Ticket.objects.get(pk=ticket_id)
    context={
        'ticket':ticket
    }
    return render(request,'ticket_details.html',context)

@login_required
def showtime_details(request,showtime_id):
    showtime=Showtime.objects.get(id=showtime_id)
    context={
        'showtime':showtime
    }
    if request.method=='POST':
        try:
            seat_count=int(request.POST['seat_count'])
            assert showtime.status==showtime.SALE_OPEN,'cant buy ticket'
            assert showtime.free_seats>=seat_count,'dont have engough free seats'
            price=showtime.price*seat_count
            assert request.user.profile.spend(price),'dont have enough money'
            showtime.reserve(seat_count)
            ticket=Ticket.objects.create(showtime=showtime,customer=request.user.profile,seat_number=seat_count)
        except Exception as e:
            context['error']=str(e)
        else:
            return HttpResponseRedirect(reverse("ticket_list"))
    return render(request,'showtime_details.html',context)