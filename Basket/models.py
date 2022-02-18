from django.db import models
from Register.models import User
from Product.models import Product
# Create your models here.
class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    order_date = models.DateField(null=True)

    @property
    def getBasketTotal(self):
        itembaskets = self.itembasket_set.all()
        total = sum([item.getTotal for item in itembaskets])
        return total

    @property
    def getBasketCount(self):
        count = self.itembasket_set.all().count()
        return count


    def __str__(self):
        return str(self.id)


class ItemBasket(models.Model):
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE, null = True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    @property
    def getTotal(self):
        total =self.product_id.price*self.quantity
        return total

    def __str__(self):
        return str(self.product_id.id)