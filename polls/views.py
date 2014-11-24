from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)


def results(request, question_id):
    response = "You are looking at results of question %s." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
