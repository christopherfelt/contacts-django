from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)


from .models import Contact
from .forms import ContactForm


class HomepageView(TemplateView):
    template_name = 'home.html'


class ContactsListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    template_name = 'contacts.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(username=self.request.user)


class ContactDetailView(LoginRequiredMixin, DetailView):
    login_url = 'account_login'
    template_name = 'detail_contact.html'
    model = Contact
    context_object_name = "contact"


class CreateContact(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    template_name = "create_contact.html"
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class UpdateContact(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    template_name = 'update_contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')


class DeleteContact(LoginRequiredMixin, DeleteView):
    login_url = 'account_login'
    template_name = 'delete_contact.html'
    model = Contact
    success_url = reverse_lazy('contacts')

