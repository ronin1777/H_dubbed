from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', "start_release_date" )
    search_fields = ('title',)
    list_filter = ('start_release_date',)
    prepopulated_fields = {'slug': ('title',)}


