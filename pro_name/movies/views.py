from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
# Create your views here.

def movies(request):
	return HttpResponse(" tmovies will be displayed here")

class list(generic.ListView):
	model = models.song
	context_object_name = 'movie_list'
	template_name = 'movies/list.html'

def detail(request,pk):
	movie = models.movielist.objects.get(pk=pk)
	return render(request,'movies/detailview.html',{'movie':movie})