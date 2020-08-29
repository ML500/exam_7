from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        form.save_m2m()
        return redirect('poll_view', pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice
    success_url = reverse_lazy('index')

