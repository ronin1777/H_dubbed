from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from h_dubbed import settings
from rating.models import Rating


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='U_posts')
    body = models.TextField(_('body'))
    slug = models.SlugField()
    title = models.CharField(_('title'), max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = GenericRelation(Rating, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    @property
    def avg_rating(self):
        ratings = Rating.objects.filter(content_type__model='post', object_id=self.id)
        if ratings.exists():
            total_ratings = sum(rating.rating for rating in ratings)
            return total_ratings / ratings.count()
        return 0


class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image_post')
    media = models.ForeignKey('media.MediaModel', on_delete=models.PROTECT, blank=True, null=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='u_comments', null=True, blank=True)
    anonymous_user = models.CharField(_('name'), max_length=200)
    email = models.EmailField(_('email'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='p_comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='r_comments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(_('body'), max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=5)