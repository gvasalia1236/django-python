from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
    return HttpResponse('''<form>
        <input type="text" placeholder="Home">
        <input type="submit" value="Enter">
        </form>''')


def contact(request):
        if request.method == 'POST':
             var = request.POST.get('name')
             return HttpResponse(f'<h1> Hello {var} </h1>')   
        return render(request, 'index.html')


def about(request):
    return HttpResponse('''<form>
        <input type="text" placeholder="About">
        <input type="submit" value="Enter">
        </form>''')


     
