from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog    # object

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    # return HttpResponse("Hello this is form app")
    return render(request,"crud/index.html",
                  {"blogs":blog}) # calling from above blog variable and :(putting) it to loop in index.html (templates)

def about(request):
    return render(request,"crud/about.html")