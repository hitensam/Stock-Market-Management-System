from django.db import models

# Create your models here.

class user(models.Model):
    user_email = models.CharField(max_length=50, primary_key=True)
    user_pass = models.CharField(max_length=60)


class stocks(models.Model):
    user_email = models.ForeignKey(user, on_delete=models.CASCADE)
    exchange = models.CharField(max_length=3, null=False)
    code = models.CharField(max_length=50, null=False)
    stock = models.CharField(max_length=50, null=False)
    today_price = models.FloatField()
    yesterday_price = models.FloatField()
    purchase_price = models.FloatField(null=False) 
    qty = models.IntegerField(default=1)