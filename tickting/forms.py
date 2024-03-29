from django import forms

from tickting.models import Cinema


class showtimesearch(forms.Form):
    movie_name=forms.CharField(max_length=100,label='movie name:',required=False)
    sale_is_open=forms.BooleanField(label='sale is open films',required=False)
    movie_length_min=forms.IntegerField(label='min length of movie:',required=False,min_value=20,max_value=200)
    movie_length_max=forms.IntegerField(label='max length of movie:',required=False,min_value=20,max_value=200)

    PRICE_ANY=0
    PRICE_UNDER_10=1
    PRICE_10_TO_30=2
    PRICE_ABOVE_30=3
    PRICE_LEVEL_CHOICES=(
        (PRICE_ANY,'ANY PRICE'),
        (PRICE_UNDER_10,'PRICE UNDER 10'),
        (PRICE_10_TO_30,'PRICE BETWEEN 10 TO 30'),
        (PRICE_ABOVE_30,'PRICE ABOVE 30')
    )
    price_level=forms.ChoiceField(label='ring of price:',choices=PRICE_LEVEL_CHOICES,required=False)
    cinema_filter=forms.ModelChoiceField(label='cinema:',queryset=Cinema.objects.all(),required=False)

    def get_price_level(self):
        price_level=self.cleaned_data['price_level']
        if price_level == showtimesearch.PRICE_UNDER_10:
            return None,10
        if price_level == showtimesearch.PRICE_10_TO_30:
            return 10,30
        if price_level == showtimesearch.PRICE_ABOVE_30:
            return 30,None
        else:
            return None,None


