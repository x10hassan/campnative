from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from campnative.index_page import IndexPage


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', IndexPage.as_view()),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^campground/', include('campground.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
