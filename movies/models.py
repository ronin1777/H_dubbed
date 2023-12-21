from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.CharField(_('slug'), max_length=255)
    start_release_date = models.DateField(_('start_release'), null=True, blank=True)
    end_release_date = models.DateField(_('end_release'), null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)