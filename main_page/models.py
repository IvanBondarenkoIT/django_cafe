from django.db import models
import uuid
import os


# Create your models here.
# About
class About(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', filename)

    title = models.CharField(max_length=100, unique=True)
    desc_body = models.TextField(max_length=400, blank=True) # Можливо висточить одного опису
    desc_bottom = models.TextField(max_length=400, blank=True) # Якщо не вистачить
    video = models.FileField(upload_to=get_file_name)


# Why Us
class WhyUs(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(max_length=400, blank=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)


# Menu
class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class Dish(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', filename)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    desc = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name)


# Specials
class Specials(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', filename)

    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100, blank=True)
    desc = models.TextField(max_length=400, blank=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name)


# Events
class Events(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', filename)
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(max_length=400, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
