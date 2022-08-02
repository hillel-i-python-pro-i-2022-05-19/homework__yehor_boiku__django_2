from django.urls import reverse_lazy

from apps.contacts.models import Contact

from django.views.generic.edit import UpdateView


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['contact_name', 'phone_number']
    template_name_suffix = '_update'
    success_url = reverse_lazy('contacts:show_all_contacts')
