from django.http import Http404
from django.views import generic
from django import forms
from django.forms import ModelForm
from django.db.models import Q

from campground.models import Campground, Amenity, Activity
from locations.models import State


class ExploreForm(ModelForm):
    name = forms.CharField(required=False)

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


class ExploreView(generic.edit.FormView):
    template_name = 'campground/explore.html'
    form_class = ExploreForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ExploreView, self).get_context_data(**kwargs)
        context.update({
            'states': State.objects.all(),
            'activities': Activity.objects.all(),
            'amenities': Amenity.objects.all(),
            'campgrounds': getattr(self, 'campgrounds', None)
        })
fortunately
        return context

    def form_valid(self, form):
        query = [
            Q(name__icontains=form.cleaned_data['name']) if 'name' in form.cleaned_data and form.cleaned_data['name'] else None,
            Q(state__name__icontains=form.cleaned_data['state']) if 'state' in form.cleaned_data and form.cleaned_data['state'] else None,
            Q(city__name__icontains=form.cleaned_data['city']) if 'city' in form.cleaned_data and form.cleaned_data['city'] else None
        ]

        for amenity in form.cleaned_data['amenities']:
            query.append(Q(amenities__name=amenity))

        for activity in form.cleaned_data['activities']:
            query.append(Q(activities__name=activity))

        self.campgrounds = Campground.objects.filter(*filter(lambda item: item, query))

        return self.render_to_response(self.get_context_data(form=form))
