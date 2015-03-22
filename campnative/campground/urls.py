from django.conf.urls import patterns, url

from campground.views import CampgroundView, ExploreView


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', CampgroundView.as_view(), name='detail'),
    url(r'^explore/$', ExploreView.as_view(), name='explore'),
)
