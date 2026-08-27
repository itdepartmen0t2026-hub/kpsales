from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('allproduct/', allproduct, name='allproduct'),
    path('product/', product, name='product'),
    path('services/', services, name='services'),
    path('career/', career, name='career'),
    path('contact/', contect, name='contact'),
    

]