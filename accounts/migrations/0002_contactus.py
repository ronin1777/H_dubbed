# Generated by Django 4.2.8 on 2023-12-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200, verbose_name='first name')),
                ('l_name', models.CharField(max_length=200, verbose_name='last name')),
                ('email', models.EmailField(max_length=200, verbose_name='email')),
                ('text', models.TextField(verbose_name='text')),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
    ]