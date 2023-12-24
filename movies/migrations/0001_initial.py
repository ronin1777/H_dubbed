# Generated by Django 4.2.8 on 2023-12-24 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1)),
                ('is_awarded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1)),
                ('is_awarded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.CharField(max_length=255, verbose_name='slug')),
                ('type', models.CharField(choices=[('movie', 'Movie'), ('anime', 'Anime'), ('tv_series', 'Tv Series')], default='movie', max_length=20)),
                ('start_release_date', models.DateField(blank=True, null=True, verbose_name='start_release')),
                ('end_release_date', models.DateField(blank=True, null=True, verbose_name='end_release')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('imdb_rating', models.FloatField(blank=True, default=0, null=True)),
                ('runtime', models.CharField(blank=True, max_length=100, null=True, verbose_name='runtime')),
                ('episodes', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('casts', models.ManyToManyField(related_name='cast_movies', to='movies.casts')),
                ('director', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_movie', to='movies.director')),
                ('genres', models.ManyToManyField(related_name='director_movies', to='movies.genre')),
            ],
        ),
    ]
