from django.contrib import admin
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    preferences = models.JSONField(default=dict)
    alt_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

class Apartment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recommended_score = models.FloatField()
    alt_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    rating = models.IntegerField()
    alt_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.apartment.title} - {self.rating}"

