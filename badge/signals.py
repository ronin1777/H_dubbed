from django.db.models.signals import post_save
from django.dispatch import receiver

from Profile.models import Profile
from .models import Badge, UserBadge
from h_dubbed import settings


def check_profile_completion(sender, instance, created, **kwargs):
    """
    update profile badge  if user fill first name and last name.
    """
    if created:

        def check_profile():
            if instance.Profile.last_name and instance.Profile.first_name:
                return True
            else:
                return False

        if check_profile:
            badge = Badge.objects.get(name="profile badge")
            user_badge = UserBadge.objects.get(user=instance.user, badge=badge)
            user_badge.progress = 100
            user_badge.save()


@receiver(post_save, sender=Profile)
def profile_save_handler(sender, instance, created, **kwargs):
    check_profile_completion(sender, instance, created, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_badge(sender, instance, created, **kwargs):
    """
    create all badge if user register
    """
    if created:
        badges = Badge.objects.all()
        for badge in badges:
            UserBadge.objects.create(badge=badge, user=instance, progress=0)


