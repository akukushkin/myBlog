from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    response = "Hello, World!<br>\nMethod:"
    response = response + request.method + "<br>\n"

    if request.method == 'GET':
        d = dict(request.GET)
    else:
        d = dict(request.POST)

    for k in d:
        line = '%s: %s<br>\n' % (k, " ".join(d[k]))
        response = response + line

    return HttpResponse(response)

#def index(request):
#    return render(request, 'templates/index.html')

#def signup(request):
#    return render(request, 'templates/signup.html')

#def login(request):
#    return render(request, 'templates/login.html')
# Create your views here.
