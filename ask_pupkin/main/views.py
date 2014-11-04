from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html', {'host': request.get_host(), 'logged_in': True, })

def signup(request):
    return render_to_response('signup.html', {'logged_in': False, 'host': request.get_host(), })

def login(request):
    return render_to_response('login.html', {'logged_in': False, 'host': request.get_host(), })
