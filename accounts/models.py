from django.db import models
from accounts.managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.core.mail import send_mail

from badge.models import Badge, UserBadge
from comment.models import Comment
from level.models import Level


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), blank=True, unique=True)
    badge = models.ManyToManyField(Badge, null=True, blank=True, through=UserBadge)
    point = models.PositiveIntegerField(default=0)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='user_lvl', null=True, blank=True)
    verified_email = models.BooleanField(default=False, error_messages='you must active your email')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        self.update_level()
        super().save(*args, **kwargs)

    def update_level(self):
        if self.level:
            next_lvl = int(self.level.level_numb + 1)
            lvl = Level.objects.filter(level_numb=next_lvl).first()
            if lvl and self.point >= lvl.required_points:
                self.level = lvl
        else:
            self.level = Level.objects.get(level_numb=1, required_points=0)


class ContactUs(models.Model):
    f_name = models.CharField(_('first name'), max_length=200)
    l_name = models.CharField(_('last name'), max_length=200)
    email = models.EmailField(_('email'), max_length=200)
    text = models.TextField(_('text'))

    class Meta:
        db_table = "contactus"
