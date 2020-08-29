from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from webapp.models import Poll
from webapp.forms import PollForm


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    paginate_by = 5
    paginate_orphans = 0
