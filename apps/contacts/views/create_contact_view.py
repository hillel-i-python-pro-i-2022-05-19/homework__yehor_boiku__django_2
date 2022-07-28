from django.urls import reverse_lazy

from apps.contacts.models import Contact

from django.views.generic.edit import CreateView


class ContactCreateView(CreateView):
    model = Contact
    fields = ['contact_name', 'phone_number']
    template_name_suffix = '_form'
    success_url = reverse_lazy('contacts:show_all_contacts')
