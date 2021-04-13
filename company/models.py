from django.db import models


class Company(models.Model):
    uuid = models.UUIDField(auto_created=True)
    name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    date_time_created = models.DateTimeField(auto_now_add=True)
