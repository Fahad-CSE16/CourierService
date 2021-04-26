from django.db import models
class Division(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class District(models.Model):
    name=models.CharField(max_length=100)
    division=models.ForeignKey(Division,on_delete=models.SET_NULL, null=True, related_name="division_set")
    def __str__(self):
        return self.name
class SubDistrict(models.Model):
    name=models.CharField(max_length=100)
    district=models.ForeignKey(District, on_delete=models.CASCADE,related_name="dis_set")
    def __str__(self):
        return self.name
class Merchant(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    email=models.EmailField()
    def __str__(self):
        return self.name
# Create your models here.
class Orders(models.Model):
    TYPE = (
        ('Fragile', 'Fragile'),
        ('Liquid', 'Liquid'),
    )
    LOCATION_TYPE = (
        ('Inside_Dhaka', 'Inside_Dhaka'),
        ('Division_of_Dhaka', 'Division_of_Dhaka'),
        ('Outside_Dhaka', 'Outside_Dhaka'),
    )
    marchant=models.ForeignKey(Merchant, on_delete=models.SET_NULL, null=True, related_name='merchant_name')
    marchant_invoice_id=models.IntegerField()
    location=models.CharField(max_length=100)
    product_type=models.CharField(max_length=50, choices=TYPE)
    location_type=models.CharField(max_length=50, choices=LOCATION_TYPE)
    weight=models.FloatField()
    price=models.FloatField(default=0)
    price_with_cod=models.FloatField(default=0)
    price_with_return_charges=models.FloatField(default=0)
    district=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='dis_name')
    subdistrict=models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, null=True, related_name='subdis_name')


    def __str__(self):
        return self.location

    