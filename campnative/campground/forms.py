from django.db import models
from django.forms import ModelForm

from campground.models import Campground


class AuthorForm(ModelForm):
    class Meta:
        model = Campground
        fields = ['name', 'activities', 'amenities', 'city', 'state']
