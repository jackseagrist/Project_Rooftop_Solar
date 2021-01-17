from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse('homepage')
    return render(request, 'index.html')