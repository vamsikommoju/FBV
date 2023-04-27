
from django.shortcuts import render

# Create your views here.


def sonu(request):
    info =['tinku','6','btech','CSE']
    context = {'info':info}
    return render(request,'app2/sonu.html',context)
