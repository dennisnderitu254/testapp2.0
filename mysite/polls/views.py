from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import  get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Choice, Question 

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		''' Return the last five published questions.'''
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

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