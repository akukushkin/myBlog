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
# Create your views here.
