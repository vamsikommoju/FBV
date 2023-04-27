
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'app1/index.html',{'msg':'This is Index Page'})


def tabu(request):
    data = ['tabusha','9','btech','ECE']
    context = {'data':data}
    return render(request,'app1/tabu.html',context)