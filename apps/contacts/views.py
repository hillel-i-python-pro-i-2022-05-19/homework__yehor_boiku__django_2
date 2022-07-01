from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm
from .models import Contact


def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(
        request,
        'contacts/show_all_contacts.html',
        {'contacts': contacts},
    )


def create_contact(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:show_all_contacts')
    else:
        form = ContactForm()

    return render(
        request,
        'contacts/edit.html',
        {'form': form},
    )


def edit(request: HttpRequest, pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)

    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:show_all_contacts')
    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        'contacts/edit.html',
        {'form': form},
    )


def delete(request: HttpRequest, pk) -> HttpResponse:
    deleted_contact, _ = Contact.objects.filter(pk=pk).delete()
    return redirect('contacts:show_all_contacts')
