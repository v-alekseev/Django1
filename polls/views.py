from django.shortcuts import render
from django.http import HttpResponse

# from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import Choice, Poll

class IndexView(generic.ListView):
   template_name = "polls/index.html"
   context_object_name = "latest_question_list"

   def get_queryset(self):
        # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
        # context = {'latest_poll_list': latest_poll_list}
        # return render(self.request, 'polls/index.html', context)
        return Poll.objects.order_by('-pub_date')[:5]

       # latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
       # output = ', '.join([p.question for p in latest_poll_list])
       # return HttpResponse(output)
       #
       # return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now11'] = timezone.now()
        context['polls_c'] = "foo"
        return context


class DetailView(generic.DetailView):
   model = Poll
   template_name = "polls/detail.html"


   # def get_queryset(self):
   #      return Poll.objects.all()

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['id'] = self.object.id
        context['polls_c'] = "foo"


        return context

# class ResultsView(generic.DetailView):
#    model = Question
#    template_name = "polls/results.html"
#
#    def vote(request, question_id):
#        p = get_object_or_404(Question, pk=question_id)
#            try:
#                selected_choice = p.choice_set.get(pk=request.POST['choice'])
#            except (KeyError, Choice.DoesNotExist):
#                return render(request, 'polls/detail.html', {
#                    'question': p,
#                    'error_message': "You didn't select a choice",
#                })
#            else:
#                selected_choice.votes += 1
#                selected_choice.save()
#                return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
