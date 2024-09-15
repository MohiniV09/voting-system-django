from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choices = request.POST.getlist('choice')
        if not selected_choices:
            raise KeyError
    except KeyError:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You did not select a choice.'
        })
    else:
        for choice_id in selected_choices:
            selected_choice = question.choice_set.get(pk=choice_id)
            selected_choice.votes += 1
            selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))