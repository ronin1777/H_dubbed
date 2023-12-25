from celery import shared_task

from comment.models import Comment
from .models import UserBadge, Badge


@shared_task
def assign_badge(user_id):
    """
    this is a task for assign comment badge to a user that have more than comment condition badge
    After that I pass it to signal to handel that
    """
    user_badge = UserBadge.objects.filter(user_id=user_id, badge__name='comment badge').first()
    badge = Badge.objects.get(name='comment badge')
    if user_badge:
        return False

    comment_count = Comment.objects.filter(user_id=user_id).count()
    if comment_count >= badge.condition:
        badge = Badge.objects.get(name='comment badge')
        UserBadge.objects.create(user_id=user_id, badge=badge, progress=100)
        return True

    return False


