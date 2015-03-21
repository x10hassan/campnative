from django.views import generic

from campground.models import Campground


class CampgroundView(generic.DetailView):
    template_name = 'campground/campground.html'
    context_object_name = 'campground'
    model = Campground
