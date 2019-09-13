from django.shortcuts import render
from realtors.models import Realtor 
from listings.models import Listing 
from listings.choices import bedroom_choices, price_choices, state_choices
# Create your views here.
def home(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {
		'listings' 			: listings,
		'state_choices'		: state_choices,
		'bedroom_choices'	: bedroom_choices,
		'price_choices' 	: price_choices,
	}
	return render(request, 'pages/home.html',context)

def about(request):
	realtors = Realtor.objects.all()
	context  = {
		'realtors': realtors
	}
	return render(request, 'pages/about.html', context)