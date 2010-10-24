from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext as
from django.contrib.comments.models import Comment


class Person(models.Model):
    """Personal information model."""
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=200)
    nickname = models.CharField(_('nickname'), max_length=100, blank=True,
            null=True)
    title = models.CharField(_('title'), max_length=200, blank=True,
            null=True)
    company = models.ForeignKey(Company)
    about = models.TextField(_('about'), blank=True, null=True)

    user = models.ForeignKey(User, blank=True, null=True, verbose_name=_('user'))

    phone_number = GenericRelation('PhoneNumber')
    email_address = GenericRelation('EmailAddress')
    instant_messenger = GenericRelation('InstantMessenger')
    web_site = GenericRelation('WebSite')
    street_address = GenericRelation('StreetAddress')
    note = GenericRelation(Comment, object_id_field='object_pk')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

