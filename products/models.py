from django.db import models

class Product(models.Model):
    title   = models.CharField(max_length=100)
    description = models.TextField(blank=True, null = True)
    price= models.DecimalField(max_digits=10,decimal_places=2)
    summary= models.CharField(max_length=100, blank=True, null=True )
    feature=models.BooleanField(default=False)


    def __str__(self):
        return self.title

   