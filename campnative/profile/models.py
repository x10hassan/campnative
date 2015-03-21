from django.db import models
from django.contrib.auth.models import User

from campnative.utils import set_upload_path
from campnative.base_model import BaseModel
from campground.models import Campground, Campsite


class Badge(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=set_upload_path)
    description = models.TextField()

    __string__ = lambda self: self.title


class Profile(BaseModel):
    user = models.OneToOneField(User)
    badges = models.ManyToManyField(Badge, through='UserBadges')
    photo = models.ImageField(upload_to=set_upload_path)
    visited_campgrounds = models.ManyToManyField(Campground, through='VisitedCampground', related_name='visited_campground')
    dream_campgrounds = models.ManyToManyField(Campground, through='DreamCampground', related_name='dream_campground')
    campground_reviews = models.ManyToManyField(Campground, through='CampgroundReview')
    campsite_reviews = models.ManyToManyField(Campsite, through='CampsiteReview')

    __string__ = lambda self: str(self.user)


class UserBadges(BaseModel):
    user = models.ForeignKey(Profile)
    badge = models.ForeignKey(Badge)
    earned_date = models.DateTimeField(auto_now=True)

    __string__ = lambda self: str(self.user)


class VisitedCampground(BaseModel):
    public = models.BooleanField(default=True)
    visit_time = models.DateTimeField()

    user = models.ForeignKey(Profile)
    campground = models.ForeignKey(Campground)

    __string__ = lambda self: str(self.user)


class DreamCampground(BaseModel):
    rank = models.IntegerField()
    public = models.BooleanField(default=True)

    user = models.ForeignKey(Profile)
    campground = models.ForeignKey(Campground)

    __string__ = lambda self: str(self.user)


class CampgroundReview(BaseModel):
    user = models.ForeignKey(Profile)
    campground = models.ForeignKey(Campground)

    text = models.TextField()
    public = models.BooleanField(default=True)
    scenery = models.IntegerField()
    comfort = models.IntegerField()
    accommodations = models.IntegerField()
    accessibility = models.IntegerField()

    __string__ = lambda self: '{} - {}'.format(str(self.user), str(self.campground))


class CampsiteReview(BaseModel):
    user = models.ForeignKey(Profile)
    campsite = models.ForeignKey(Campsite)

    text = models.TextField()
    public = models.BooleanField(default=True)
    scenery = models.IntegerField()
    comfort = models.IntegerField()
    accommodations = models.IntegerField()
    accessibility = models.IntegerField()

    __string__ = lambda self: '{} - {}'.format(str(self.user), str(self.campground))
