# Picture Search By Geolocation

We have used `Django` framework of Python and `Bootstrap` as a CSS framework.

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

## Go to live link

- Live app: https://flicker-project.herokuapp.com/
- Admin app: https://flicker-project.herokuapp.com/admin/
    - username : admin@gmail.com
    - password : admin

## SetUp Project


### Create a Virtual Environment

```sh 
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```

### Run the project

You can check the link http://127.0.0.1:8000.

```sh 
python manange.py runserver 0.0.0.0
```

### Create a superuser for admin site

```sh 
python manange.py createsuperuser
```

### Admin site

http://127.0.0.1:8000/admin

- After you login in the admin site, Click on `Preset Location` and then you can able to add new location. 

- Search result stored in `Location`.

- User favourite photo stored in `UserFavouriteList`.

- Preset location stored in `AddPresetLocation`.
