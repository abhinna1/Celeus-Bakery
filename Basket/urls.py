from django.urls import path
from . import views

urlpatterns = [
    path('', views.getBasket),
    path('insertbasket/<int:product_id>', views.insertBasket, name='insertBasket'),
    path('removebasket/<int:id>', views.removeBasket, name='removeBasket'),
]