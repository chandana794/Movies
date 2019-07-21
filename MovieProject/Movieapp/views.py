from django.shortcuts import render
from . import Forms
from Movieapp.models import Movies

def index_View(request):
    return render(request,'Movieapp/Index.html')

def Movieview(request):
    if request.method=='GET':
        form=Forms.MoviesForm()
        print("display form to user")

    if request.method=='POST':
        form=Forms.MoviesForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return index_View(request)
    return render(request,'Movieapp/AddMovies.html',{'form':form})

def listview(request):
    Movies_list= Movies.objects.all()
    return render(request,'Movieapp/ListMovie.html',{'Movies_list':Movies_list})





# Create your views here.
