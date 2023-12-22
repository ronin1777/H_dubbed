from django.db.models.signals import pre_save
from django.dispatch import receiver

from media.exceptions import DuplicateImageException
from media.models import MediaModel


@receiver(pre_save, sender=MediaModel)
def check_duplicate_hash(sender, instance, **kwargs):
    existed = MediaModel.objects.filter(file_hash=instance.file_hash).exclude(pk=instance.pk).exists()
    if existed:
        raise DuplicateImageException("Duplicate")