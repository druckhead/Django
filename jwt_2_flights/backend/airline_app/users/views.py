from django.http import HttpResponse


def index(request):
    return HttpResponse('users index.html')
