from django.views import generic

from campground.models import Activity, Amenity


class IndexPage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)

        context.update({
            'activities': Activity.objects.all(),
            'amenities': Amenity.objects.all(),
        })

        return context
