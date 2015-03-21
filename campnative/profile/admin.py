from django.contrib.auth.models import User
from django.contrib import admin

from profile.models import Badge, Profile, CampgroundReview, CampsiteReview, DreamCampground, VisitedCampground

admin.site.register(Badge)
admin.site.register(CampgroundReview)
admin.site.register(CampsiteReview)
admin.site.register(DreamCampground)
admin.site.register(VisitedCampground)

# admin.site.unregister(User)
admin.site.register(Profile)
