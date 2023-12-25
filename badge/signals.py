from django.db.models.signals import post_save
from django.dispatch import receiver

from Profile.models import Profile
from comment.models import Comment
from .models import Badge, UserBadge


def check_profile_completion(sender, instance, created, **kwargs):
    """
    assign profile badge to users if they fill first name and last name.
    """
    if created:

        def check_profile():
            if instance.Profile.last_name and instance.Profile.first_name:
                return True
            else:
                return False

        if check_profile:
            badge = Badge.objects.get(name="profile badge")
            user_badge = UserBadge(user=instance.user, badge=badge, progress=100)
            user_badge.save()


@receiver(post_save, sender=Profile)
def profile_save_handler(sender, instance, created, **kwargs):
    check_profile_completion(sender, instance, created, **kwargs)




