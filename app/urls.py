from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(pattern_name='places')),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('places', views.photo_search, name="places"),
    path('favourite-list', views.FavouriteListView.as_view(), name="favourite-list"),
    path('add-to-favourite', views.add_to_favourite_list, name="add-to-favourite"),
]
