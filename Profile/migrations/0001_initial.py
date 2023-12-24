# Generated by Django 4.2.8 on 2023-12-24 15:06

import Profile.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female')], max_length=1, null=True)),
                ('age', models.SmallIntegerField(blank=True, default=10, null=True, verbose_name='age')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('phon_number', models.CharField(blank=True, max_length=13, null=True, validators=[Profile.validators.IranianMobileNumberValidator()], verbose_name='Mobile Number')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
