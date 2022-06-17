from django.shortcuts import render
from .models import Director, Movie, MovieInstance, Genre
from django.views import generic
from django.http import Http404
# Create your views here.

def index(request):
    num_movies=Movie.objects.all().count()
    num_instances=MovieInstance.objects.all().count()
    disponibles=MovieInstance.objects.filter(status__exact='d').count
    num_directores = Director.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_movies':num_movies,
            'num_directores':num_directores,
            'disponibles':disponibles,
            'num_instances':num_instances,
        }
    )

class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 8

class MovieDetailView(generic.DetailView):
    model = Movie

class DirectorListView(generic.ListView):
    model= Director
    paginate_by = 8

class DirectorDetailView(generic.DetailView):
    model = Director
    
    