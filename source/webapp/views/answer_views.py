from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import AnswerForm
from webapp.models import Answer


class AnswerView(View):
    form_class = AnswerForm
    template_name = 'answer/answer_view.html'
    redirect_url = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return render(self.request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        return kwargs

    def get_redirect_url(self):
        return self.redirect_url
