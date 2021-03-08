# Picture Search By Geolocation

## Challenge Description 
Write a responsive application that search for pictures using Flickr API, based on user input and present the results.

This challenge is designed to test your ability to write code that inter-operates with a third-party API as well as develop a simple user interface.

## Challenge Specification
The user should be able to:
- Search for a location, and see the thumbnails of the first 10 photos available for that location. Navigation should be available to get the next 10 photos
- Perform the search either by entering latitude and longitude, or selecting a location from a preset list. Locations in the preset list should be represented by a human-readable name.
- Add entries to the preset list by supplying a longitude, latitude and name. **This list should be stored in the backend.
- Add photos in a search result to a favourites list. **This list should be stored in the backend.
- View thumbnails of the photos in the favourite list
- Your frontend should not connect to Flickr API directly.

# SetUp Project

Make sure python3 install on your machine.

## Install virtual enviornment 

```sh 
python3 -m pip install --user virtualenv
```

## Creating a virtual environment

```sh 
python3 -m venv env
```

## Activating a virtual environment
```sh 
source env/bin/activate
```


## run the following command for project setup.

```sh 
python manange.py runserver
```


## Create a superuser for admin site.

```sh 
python manange.py createsuperuser
python manange.py runserver
```

## Urls for admin site
http://127.0.0.1:8000/admin

- After you can login on admin site click on Preset Location you able to add pre location. 

- Search result stored in Location module.

- User favourite photo stored in UserFavouriteList module.

- Preset location stored in AddPresetLocation.
