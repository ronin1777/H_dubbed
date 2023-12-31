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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='body')),
                ('slug', models.SlugField()),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='U_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='media.mediamodel')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_post', to='comment.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous_user', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('is_reply', models.BooleanField(default=False)),
                ('body', models.TextField(max_length=400, verbose_name='body')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_comments', to='comment.post')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_comments', to='comment.comment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='u_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
