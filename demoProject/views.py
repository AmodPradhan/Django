from django.http import HttpResponse

def homepage(request):
   
    return HttpResponse("Hello, world. You're at the polls index.")