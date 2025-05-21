from django.db import models

class Engine(models.Model):

    image = models.ImageField(upload_to="e_images/", null=True, blank=True)

class Logistic(models.Model):

    image = models.ImageField(upload_to="l_images/", null=True, blank=True)

class Handyman(models.Model):

    image = models.ImageField(upload_to="h_images/", null=True, blank=True)