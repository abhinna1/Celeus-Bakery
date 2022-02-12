from lib2to3.pytree import Base
from django.contrib import admin
from .models import Basket, ItemBasket
# Register your models here.
admin.site.register(Basket)
admin.site.register(ItemBasket)