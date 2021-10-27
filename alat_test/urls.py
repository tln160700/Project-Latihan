from django.urls import path
from alat_test import views


urlpatterns = [ 
    path('', views.home, name='Home')
]
