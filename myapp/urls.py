

from django.urls import path
from . import views


urlpatterns = [
    path('myip/', views.waht_is_my_ip),
   
    path('home/',views.home)
    #path('about/', views.about),
    #path('contact/', views.contact),

]
