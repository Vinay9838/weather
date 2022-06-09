from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

