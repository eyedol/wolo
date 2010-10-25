from django.conf.urls.defaults import *

urlpatterns = patterns('wolo.contacts.views',
	(r'^$', 'list'),
)
