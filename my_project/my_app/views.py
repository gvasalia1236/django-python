from django.http import HttpResponse

def home(request):
    return HttpResponse('This is home page')

def about(request):
    return HttpResponse('This is about page')


def contact(request):
    return HttpResponse('This is contact page')

def website(request):
    return HttpResponse('This is website')
