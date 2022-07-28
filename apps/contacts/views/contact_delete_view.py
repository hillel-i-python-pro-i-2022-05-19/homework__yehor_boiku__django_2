from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from apps.contacts.models import Contact


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:show_all_contacts')
