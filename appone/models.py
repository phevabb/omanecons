from django.db import models
from django.urls import reverse

class Engine(models.Model):
    image = models.ImageField(upload_to="e_images/", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    image_alt = models.CharField(max_length=255, blank=True, verbose_name="Image Alt Text")

    def get_absolute_url(self):
        return reverse("engine_detail", args=[str(self.id)])

class Logistic(models.Model):
    image = models.ImageField(upload_to="l_images/", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    image_alt = models.CharField(max_length=255, blank=True, verbose_name="Image Alt Text")

    def get_absolute_url(self):
        return reverse("logistic_detail", args=[str(self.id)])

class Handyman(models.Model):
    image = models.ImageField(upload_to="h_images/", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    image_alt = models.CharField(max_length=255, blank=True, verbose_name="Image Alt Text")

    def get_absolute_url(self):
        return reverse("handyman_detail", args=[str(self.id)])
