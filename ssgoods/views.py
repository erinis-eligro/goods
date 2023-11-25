from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Adobe Day!")

def input_list(request):
    return render(request, 'ssgoods/input_list.html', {})
