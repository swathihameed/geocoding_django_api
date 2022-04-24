

from django.urls import path
from . import views

urlpatterns = [
        
        path("getAddressDetails", views.result_view, name="result"),
        path("", views.input_view, name = "home"),
       

]
