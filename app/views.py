import flickrapi
import reverse_geocoder as geocoder
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import UserCreationForm
from .models import AddPresetLocation, Location, UserFavouriteList


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('places')
    template_name = 'signup.html'

    def form_valid(self, form):
        """After successful registration, login in the system.
        """
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        return response


def photo_search(request):
    """Photo search on flicker based on latitude, longtitude and name.
    """
    if request.user.is_authenticated:
        preset_location = AddPresetLocation.objects.all()
        if request.GET.get('latitude') and request.GET.get('longtitude'):
            latitude = request.GET.get('latitude')
            longtitude = request.GET.get('longtitude')
            page_num = request.GET.get('page', 1)
            coordinates = (float(latitude), float(longtitude))
            try:
                result = geocoder.search(coordinates)
                Location.objects.create(
                    latitude=float(latitude),
                    longtitude=float(longtitude),
                    place=result[0]['name'])

                flickr = flickrapi.FlickrAPI(
                    settings.API_KEY, settings.SECRET_API_KEY)

                photo_list = flickr.photos.search(
                    api_key=settings.API_KEY,
                    media='photos',
                    lat=latitude,
                    lon=longtitude,
                    accuracy=11,
                    format='parsed-json',
                    per_page=10 * int(page_num),
                    extras='url_m, url_q')

                return render(request, 'place.html', {
                    'photos_list': photo_list['photos']['photo'],
                    'location_name': result[0]['name'],
                    'latitude': latitude,
                    'longtitude': longtitude, 'preset_location': preset_location,
                    'next_url': '%s?latitude=%s&longtitude=%s&page=%s' % (reverse('places'), latitude, longtitude, int(page_num) + 1)})

            except Exception as e:
                return render(request, 'place.html', {'errors': str(e).replace('Error: 999:', '')})
        else:
            return render(request, 'place.html', {'preset_location': preset_location})
    else:
        return render(request, 'registration/login.html')


def add_to_favourite_list(request):
    """Add photos in a search result to a favourites list.
    """
    if request.user.is_authenticated:

        if request.method == 'POST':
            UserFavouriteList.objects.create(
                title=request.POST.get('title'),
                image_url=request.POST.get('image_url'),
                latitude=request.POST.get('latitude'),
                longtitude=request.POST.get('longtitude'),
                thumb_url=request.POST.get('thumb_url'),
                user=request.user)

        return JsonResponse({
            'success': 'true'
        })
    else:
        return render(request, 'registration/login.html')


class FavouriteListView(LoginRequiredMixin, generic.ListView):
    """All favourites photos display.
    """
    model = UserFavouriteList
    template_name = "favourites.html"
    paginate_by = 12
