from django.http import HttpResponse


def index(request):
    return HttpResponse('flights index.html')
