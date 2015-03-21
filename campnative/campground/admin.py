from django.contrib import admin

from campground.models import Campground, Campsite, Activity, Amenity, PhotoGallery, CampgroundAmnity, CampgroundActivity


admin.site.register(Campground)
admin.site.register(Campsite)
admin.site.register(Activity)
admin.site.register(Amenity)
admin.site.register(PhotoGallery)
admin.site.register(CampgroundAmnity)
admin.site.register(CampgroundActivity)
