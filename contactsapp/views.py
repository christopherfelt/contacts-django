from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)


from .models import Contact


class HomepageView(TemplateView):
    template_name = 'home.html'


# TODO ListView
class ContactsListView(LoginRequiredMixin, ListView):
    template_name = 'contacts.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(username=self.request.user)


class ContactDetailView(DetailView):
    template_name = 'detail_contact.html'
    model = Contact
    context_object_name = "contact"


class CreateContact(CreateView):
    template_name = "create_contact.html"
    model = Contact
    fields = ['name', 'number', 'emergency']
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class UpdateContact(UpdateView):
    template_name = 'update_contact.html'
    model = Contact
    fields = ['name', 'number', 'emergency']
    success_url = reverse_lazy('contacts')


class DeleteContact(DeleteView):
    template_name = 'delete_contact.html'
    model = Contact
    success_url = reverse_lazy('contacts')

