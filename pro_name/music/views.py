from django.shortcuts import render# Create your views here.
from django.http import HttpResponse
def music(request):
    if request.user.is_authenticated():
        movies=models.movielist.objects.all()
        return render(request,'music/home.html'{'movie_list:movies'})
    else:
        return HttpResponse("you need to login to access songs")

def listsong(request, pk):
    movie=models.movielist.objects.get(pk=pk)
    return render(request,'music/list.html',{'album':movie})