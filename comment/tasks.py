
from celery import shared_task

from badge.models import UserBadge, Badge
from comment.models import Comment


@shared_task
def update_comment_badge(user_id):
    """
    this task update progres for comment badge for all user.
    i pass it to signal
    """
    badge = Badge.objects.get(name='comment badge')
    user_badge = UserBadge.objects.get(badge=badge, user_id=user_id)
    comment_count = Comment.objects.filter(user_id=user_id).count()
    progress = round(comment_count / badge.condition * 100)
    if comment_count < badge.condition:
        user_badge.progress = progress
        user_badge.save()
    else:
        user_badge.progress = 100
        user_badge.save()




