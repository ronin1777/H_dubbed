# Generated by Django 4.2.8 on 2023-12-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_numb', models.IntegerField(blank=True, null=True)),
                ('required_points', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
