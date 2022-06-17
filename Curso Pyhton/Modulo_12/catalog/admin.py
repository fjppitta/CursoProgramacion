from django.contrib import admin
admin.autodiscover()

# Register your models here.

from .models import Director, Genre, Movie, MovieInstance

admin.site.register(Genre)

#class MoviesInline(admin.TabularInline):
#    model = Movie

#admin.site.register(Director)
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display=('primer_apellido','primer_nombre','fecha_de_nacimiento','fecha_de_muerte')
    fields = ['primer_nombre', 'primer_apellido', ('fecha_de_nacimiento', 'fecha_de_fallecimiento')]
#    inlines = [MoviesInline]


#admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=('titulo','director','anio')


admin.site.register(MovieInstance)