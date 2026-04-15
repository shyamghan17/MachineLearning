from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello world: + home')

def about(request):
    check = 4 + 4
    return HttpResponse(f'Hello world: = about, check = {check}')

def contacts(request):
    return HttpResponse('Hello world: - contacts')