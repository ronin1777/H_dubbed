from django.db import models

from comment.models import Comment
from h_dubbed import settings


class Badge(models.Model):
    class TypeBadgeChoice(models.TextChoices):
        cooper = 'cooper'
        silver = 'silver'
        gold = 'gold'
        diamond = 'diamond'

    name = models.CharField(max_length=100)
    type_badge = models.CharField(max_length=10, choices=TypeBadgeChoice.choices, default=TypeBadgeChoice.cooper)
    description = models.TextField()
    condition = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class BadgeMedia(models.Model):
    badge = models.ManyToManyField(Badge, related_name='user_badge')
    media = models.ForeignKey('media.MediaModel', on_delete=models.PROTECT)


class UserBadge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    progress = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} get {self.badge}'
