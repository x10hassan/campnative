from django.db import models

from campnative.utils import set_upload_path
from campnative.base_model import BaseModel
from locations.models import State, City


class Amenity(BaseModel):
    name = models.CharField(max_length=30)

    __string__ = lambda self: self.name


class Activity(BaseModel):
    name = models.CharField(max_length=30)

    __string__ = lambda self: self.name


class Campground(BaseModel):
    address = models.CharField(max_length=100)
    activities = models.ManyToManyField(Activity, blank=True, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to=set_upload_path)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    state = models.ForeignKey(State, blank=True, null=True)
    website = models.URLField(blank=True)
    zip_code = models.IntegerField(blank=True, null=True)

    __string__ = lambda self: self.name


class Campsite(BaseModel):
    image = models.ImageField(upload_to=set_upload_path)
    address = models.CharField(max_length=80)
    name = models.CharField(max_length=30)
    description = models.TextField()
    campground = models.ForeignKey(Campground)

    __string__ = lambda self: self.name


class PhotoGallery(BaseModel):
    image = models.ImageField(upload_to=set_upload_path)
    description = models.CharField(max_length=100, blank=True)
    image_date = models.DateTimeField(blank=True)
    campground = models.ForeignKey(Campground)

    __string__ = lambda self: self.description
