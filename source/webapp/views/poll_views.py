from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Poll
from webapp.forms import PollForm


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    paginate_by = 5
    paginate_orphans = 0
    ordering = ['-created_at']

class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll
    paginate_choices_by = 10
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        choices, page, is_paginated = self.paginate_choices(self.object)
        context['choices'] = choices
        context['page_obj'] = page
        context['is_paginated'] = is_paginated  # page.has_other_pages()

        return context

    def paginate_choices(self, poll):
        choices = poll.pols.all()
        if choices.count() > 0:
            paginator = Paginator(choices, self.paginate_choices_by, orphans=self.paginate_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return choices, None, False


class PollCreateView(CreateView):
    template_name = 'poll/poll_create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    template_name = 'poll/poll_update.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('index')


def poll_mass_action_view(request):
    if request.method == 'POST':
        ids = request.POST.getlist('selected_polls', [])
        if 'delete' in request.POST:
            Poll.objects.filter(id__in=ids).delete()
    return redirect('index')
