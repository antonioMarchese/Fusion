from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from .models import Service, Teammate
from .forms import ContactForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['teammates'] = Teammate.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "Email enviado com sucesso.")
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar o email.")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

class TesteView(FormView):
    template_name = '404.html'

class ServerError(FormView):
    template_name = '500.html'