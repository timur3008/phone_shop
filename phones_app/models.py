from django.db import models



class Brand(models.Model):
    name_brand = models.CharField(max_length=20, primary_key=True)
    def __str__(self):
        return f'{self.name_brand.title()}'
    
    
class Phone(models.Model):
    name_phone = models.CharField(max_length=20)
    image = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.FloatField()
    memory = models.SmallIntegerField()
    color = models.CharField(
        max_length=20
    )
    cart = models.BooleanField(default=False)
    description = models.TextField()
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones')
    
class Screen(models.Model):
    picture = models.ImageField()   
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE) 
    def __str__(self):
        return f'/{self.picture}'
    
