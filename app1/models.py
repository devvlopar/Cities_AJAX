from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.country_name

class Cities(models.Model):
    city_name = models.CharField(max_length=150)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self) :
        return self.city_name + ' from ' + self.country.country_name


class User(models.Model):
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.first_name


