from django.db import models

from campnative.base_model import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=40)

    __string__ = lambda self: self.name


class State(BaseModel):
    name = models.CharField(max_length=40)
    slogan = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    country = models.ForeignKey(Country)

    __string__ = lambda self: self.name


class City(BaseModel):
    name = models.CharField(max_length=40)
    state = models.ForeignKey(State)

    __string__ = lambda self: self.name
