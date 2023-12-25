# from celery import shared_task
# from django.contrib.auth import get_user_model
#
# from accounts.models import User
# from comment.models import Comment
# from .models import UserBadge, Badge
#
#
# @shared_task
# def assign_badge(user_id):
#     """
#     this is a task for assign comment badge to a user that have more than comment condition badge.
#     """
#     user_badge = UserBadge.objects.filter(user_id=user_id, badge__name='comment-badge').first()
#     badge = Badge.objects.get(name='comment-badge')
#     if user_badge:
#         return False
#
#     comment_count = Comment.objects.filter(user_id=user_id).count()
#     if comment_count >= badge.condition:
#         badge = Badge.objects.get(name='comment-badge')
#         user_badge = UserBadge.objects.create(user_id=user_id, badge=badge, progress=100)
#         user_badge.save()

