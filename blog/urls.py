from django.conf.urls import patterns, url
from blog import views

# Match blank string
urlpatterns = patterns('',
    url(r'^$', views.archive, name="archive"),
)
