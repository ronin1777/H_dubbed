from celery import shared_task

from badge.models import Badge, UserBadge
from quiz.models import QuizTaker





# @shared_task
# def assign_quiz_badge(user_id):
#     """
#     admin must create this badge in database with names('quiz beginner', 'quiz advance', 'quiz pro')
#     """
#     quiz = QuizTaker.objects.filter(user_id=user_id, is_passed=True).count()
#     if 10 > quiz >= 5:
#         badge = Badge.objects.get(name='quiz beginner')
#         UserBadge.objects.create(user_id=user_id, badge=badge)
#     elif 40 > quiz >= 20:
#         badge = Badge.objects.get(name='quiz advance')
#         UserBadge.objects.create(user_id=user_id, badge=badge)
#     else:
#         badge = Badge.objects.get(name='quiz pro')
#         UserBadge.objects.create(user_id=user_id, badge=badge)

