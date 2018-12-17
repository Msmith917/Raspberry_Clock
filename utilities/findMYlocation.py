import geocoder
location = geocoder.google('me')
print(location.city)