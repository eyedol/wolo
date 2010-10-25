from django.conf.urls.defaults import *

urlpatterns = patterns('wolo.contacts.views',
    (r'^$', 'list'),
    (r'^add/$','person.add'),
)
