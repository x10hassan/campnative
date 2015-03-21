from django.conf.urls import patterns, url

from campground.views import CampgroundView


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', CampgroundView.as_view(), name='detail'),
)
