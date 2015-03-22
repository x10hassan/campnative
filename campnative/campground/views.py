from django.views import generic
from django import forms
from django.forms import ModelForm

from campground.models import Campground, Amenity, Activity
from locations.models import State


class ExploreForm(ModelForm):
    class Meta:
        model = Campground
        fields = ['name', 'activities', 'amenities', 'city', 'state']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-required': 'true',
                'placeholder': 'If Known : Enter Name'
            }),
            'amenities': forms.CheckboxSelectMultiple(),
            'activities': forms.CheckboxSelectMultiple(),
        }


class CampgroundView(generic.DetailView):
    template_name = 'campground/campground.html'
    context_object_name = 'campground'
    model = Campground


class ExploreView(generic.edit.ProcessFormView, generic.ListView):
    template_name = 'campground/explore.html'
    model = Campground
    form_class = ExploreForm

    def get_form_class(self):
        return ExploreForm

    def get_queryset(self):
        import ipdb; ipdb.set_trace()
        query = {
            'name__icontains': self.kwargs.get('name', None),
            'state__name__icontains': self.kwargs.get('state', None),
            'city__name__icontains': self.kwargs.get('city', None),
        }

        # try:
        #     name = self.kwargs['name']
        # except:
        #     name = ''
        # if (name != ''):
        #     object_list = self.model.objects.filter(name__icontains=name)
        # else:
        #     object_list = self.model.objects.all()
        # return object_list

    def get_context_data(self, **kwargs):
        context = super(ExploreView, self).get_context_data(**kwargs)
        context.update({
            'states': State.objects.all(),
            'activities': Activity.objects.all(),
            'amenities': Amenity.objects.all(),
            'form': self.form_class
        })

        return context
