
import hashlib

from django.db import models

from bucket import bucket
from .exceptions import DuplicateImageException


# Create your models here.
class MediaModel(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    my_file = models.FileField( null=True, blank=True)
    image = models.ImageField(width_field="width", height_field="height", null=True, blank=True)
    video = models.FileField(upload_to="video/", null=True, blank=True)
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)

    file_hash = models.CharField(max_length=40, db_index=True, editable=False)
    file_size = models.PositiveIntegerField(null=True, editable=False)

    focal_point_x = models.PositiveIntegerField(null=True, blank=True)
    focal_point_y = models.PositiveIntegerField(null=True, blank=True)
    focal_point_width = models.PositiveIntegerField(null=True, blank=True)
    focal_point_height = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.image.file.closed:
            self.file_size = self.image.size

            hasher = hashlib.sha1()
            for chunk in self.image.file.chunks():
                hasher.update(chunk)

            self.file_hash = hasher.hexdigest()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BucketObjects(models.Model):
    my_file = models.FileField()
