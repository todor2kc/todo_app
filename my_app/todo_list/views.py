from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {'first_name':'1Stefan', 'last_name': 'Todorovic'}
    return render(request, 'about.html', context)