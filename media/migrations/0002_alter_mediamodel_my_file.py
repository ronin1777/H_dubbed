# Generated by Django 5.0 on 2023-12-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamodel',
            name='my_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]