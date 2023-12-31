# Generated by Django 4.2.8 on 2023-12-29 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_badge', models.CharField(choices=[('cooper', 'Cooper'), ('silver', 'Silver'), ('gold', 'Gold'), ('diamond', 'Diamond')], default='cooper', max_length=10)),
                ('description', models.TextField()),
                ('condition', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveIntegerField()),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badge.badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BadgeMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.ManyToManyField(related_name='user_badge', to='badge.badge')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='media.mediamodel')),
            ],
        ),
    ]
