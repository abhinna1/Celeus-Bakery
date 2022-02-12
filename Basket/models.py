from django.db import models
from Register.models import User
from Product.models import Product
# Create your models here.
class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class ItemBasket(models.Model):
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.product_id.id)