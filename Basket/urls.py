from django.urls import path
from . import views

urlpatterns = [
    path('', views.getBasket),
    path('insertbasket', views.insertBasket, name='insertBasket'),
]