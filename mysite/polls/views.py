from django.http import Http404
from django.shortcuts import  get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.urls import reverse
from .models import Choice, Question 

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = { 'latest_question_list': latest_question_list, }
	return render(request, 'polls/index.html', context)

# Raising 404 error using exeptions
def details(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	# response = "You're looking at the results of question %s."
	# return HttpResponse(response % question_id)
	question= get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	# return HttpResponse("You're voting on question %s." % question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/details.html' ,{
			'question':question,
			'error_message':"You didn't select a choice.",
			})
	else:
		select_choice.votes += 1
		selected_choice.save()
		# Always return an HTTPResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back Button
		return HTTPResponseRedirect(reverse('polls:results',
			args=(question.id,)))