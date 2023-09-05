from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)  # Store hashed passwords securely
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])

    def __str__(self):
        return self.username