from django.contrib import admin
from .models import Contact, DetailForContact


class InlineDetailForContact(admin.TabularInline):
    model = DetailForContact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = (InlineDetailForContact,)
