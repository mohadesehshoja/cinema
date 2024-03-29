from django.db import models

# Create your models here.
class Movie(models.Model):
    """
    Represents a movie
    """
    name=models.CharField(max_length=100)
    director=models.CharField(max_length=50)
    year=models.IntegerField()
    length=models.IntegerField()
    description=models.TextField()
    poster=models.ImageField("poster",upload_to="movie_posters/",blank=True)

    def __str__(self): #zman print be in formt print mikond object class ra
        return self.name

class Cinema(models.Model):
    """"
    Represents a cinema saloon
    """
    # cinema_code=models.IntegerField(primary_key=True) be onvan id class kar mikond
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    capacity=models.IntegerField()
    phone=models.CharField(max_length=20,null=True)
    address=models.TextField()
    poster = models.ImageField("poster", upload_to="movie_posters/",null=True,blank=True)

    def __str__(self):
        return self.name

class Showtime(models.Model):
    """
    Represents a showtime of a movie in a cinema
    """
    movie=models.ForeignKey('Movie',on_delete=models.PROTECT)
    cinema=models.ForeignKey('Cinema',on_delete=models.PROTECT)
    start_time=models.DateTimeField()
    price=models.IntegerField()
    salable_seats=models.IntegerField()
    free_seats=models.IntegerField()
    SALE_NOT_STARTED=1
    SALE_OPEN=2
    TICKETS_SOLD=3
    SALE_CLOSED=4
    MOVIE_PLAYED=5
    SHOW_CANCELED=6
    status_choice=(
        (SALE_NOT_STARTED,"sale not started"),
        (SALE_OPEN,"sale opened"),
        (TICKETS_SOLD,"tickets sold"),
        (SALE_CLOSED,"sale closed"),
        (MOVIE_PLAYED,"movie played"),
        (SHOW_CANCELED,"show cancelled")
    )
    status=models.IntegerField(choices=status_choice)
    def __str__(self):
        return f"{self.movie}-{self.cinema}-{self.start_time}"
    def reserve(self,seats):
        if seats<self.free_seats:
            self.free_seats-=seats
            self.save()
            return True
        elif seats==self.free_seats:
            self.free_seats=0
            self.status=self.TICKETS_SOLD
            self.save()
            return True
        else:
            self.save()
            return False



class Ticket(models.Model):
    showtime=models.ForeignKey('Showtime',on_delete=models.PROTECT,verbose_name='showtime')
    customer=models.ForeignKey('account.profile',on_delete=models.PROTECT,verbose_name='customer')
    seat_number=models.IntegerField('seat number')
    order_time=models.DateTimeField('order time',auto_now_add=True)
    def __str__(self):
        return "{}-{}-{}".format(self.seat_number,self.customer,self.showtime.movie)












