from .views import home,about,contact,website
from django.urls import path
urlpatterns = [
    path('', website),
    path('home/', home),
    path('about/', about),
    path('contact/', contact)
]