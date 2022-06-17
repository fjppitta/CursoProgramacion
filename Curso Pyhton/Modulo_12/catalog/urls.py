from operator import index
from django.conf.urls import url
from catalog import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^movies/$', views.MovieListView.as_view(), name='movies'),
    url(r'^movie/(?P<pk>\d+)$', views.MovieDetailView.as_view(), name='movie-detail'),
    url(r'^directores/$', views.DirectorListView.as_view(), name='directores'),
    url(r'^director/(?P<pk>\d+)$', views.DirectorDetailView.as_view(), name='director-detail'),
]
