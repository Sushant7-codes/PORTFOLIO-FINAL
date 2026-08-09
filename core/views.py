from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def page_not_found(request, exception=None):
    return render(request, 'core/404.html', status=404)
