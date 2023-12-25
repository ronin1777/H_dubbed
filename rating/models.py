from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts.models import User


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='u_votes')
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = [
            models.Index(fields=['content_type', 'object_id'])
        ]

        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return f'{self.user} rate to {self.content_object}'
