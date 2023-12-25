from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from h_dubbed import settings
from rating.models import Rating


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='U_posts')
    body = models.TextField(_('body'))
    slug = models.SlugField()
    title = models.CharField(_('title'), max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = GenericRelation(Rating, blank=True, null=True)

    class Meta:
        ordering = ['-created']
        
