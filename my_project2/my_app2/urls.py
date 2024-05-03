from .views import name
from django.urls import path

urlpatterns = [
    path('website/<str:name>', name),

]   