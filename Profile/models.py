from django.db import models

from Profile.validators import IranianMobileNumberValidator
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    GENDER = (
        ('M', 'male'),
        ('F', 'female'),
    )

    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField( blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    age = models.SmallIntegerField(_('age'), default=10, blank=True, null=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    phon_number = models.CharField(_('Mobile Number'), max_length=13,
                                   validators=[IranianMobileNumberValidator()], blank=True, null=True)
    bio = models.TextField(_('bio'), blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            full_name = f"{self.first_name} {self.last_name}"
        else:
            full_name = None
        return full_name

