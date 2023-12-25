from django.db.models.signals import post_save
from django.dispatch import receiver

from comment.models import Comment
from .tasks import assign_badge


@receiver(post_save, sender=Comment)
def give_badge(sender, instance, created, **kwargs):
    if created:
        assign_badge.delay(instance.user.id)
