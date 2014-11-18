from django.shortcuts import render_to_response
from models import Question, Tag, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request, sort='new'):
    page = request.GET.get('page')
    order = sort == 'best' and '-author__rating' or '-date_added'
    question_list = Question.objects.order_by(order)

    paginator = Paginator(question_list, 3)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    isBest = sort == 'best' and True or False 
    return render_to_response('index.html', {'logged_in': True, 'questions': questions, 'isBest': isBest})

def signup(request):
    return render_to_response('signup.html', {'logged_in': False})

def login(request):
    return render_to_response('login.html', {'logged_in': False})

def answer(request):
    id_q = request.GET.get('id_q')
    answer_list = Answer.objects.filter(question_id=id_q)
    paginator = Paginator(answer_list, 3)

    page = request.GET.get('page')
    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        answers = paginator.page(1)
    except EmptyPage:
        answers = paginator.page(paginator.num_pages)
    question = Question.objects.get(id=id_q) 
    return render_to_response('answer.html', {'logged_in': False, 'answers': answers, 'question': question})
