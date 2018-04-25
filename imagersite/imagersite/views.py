from django.shortcuts import render


def home_view(request):
    """ this view is for homepage"""
    return render(request, 'generic/home.html', {'message': 'Hello World'})
