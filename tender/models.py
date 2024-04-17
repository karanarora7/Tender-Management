from django.db import models

# Create your models here.

class Tender(models.Model):
    Hospital=models.CharField(max_length=200)
    Tender_number=models.CharField(max_length=200)
    Product=models.CharField(max_length=200)
    Location=models.CharField(max_length=200)
    Remarks=models.CharField(max_length=500)
    Tender_Won_By=models.CharField(max_length=200)
    Winning_Price=models.CharField(max_length=20)
    Date=models.DateField(auto_now=False, auto_now_add=False)
    Active = models.BooleanField(default=True)

    def __str__(self):
        return self.Hospital
