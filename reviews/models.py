from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType

from h_dubbed import settings

# Create your models here.


class Reviews(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='u_like')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.user} like {self.content_object}'

