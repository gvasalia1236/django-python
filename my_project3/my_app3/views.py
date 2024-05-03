from django.http import HttpResponse

def odd_or_even(request, id):
    if (id % 2 == 0):
        return HttpResponse('The number is even')
    else:
        return HttpResponse('The number is odd')