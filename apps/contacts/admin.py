from django.contrib import admin
from .models import Contact, DetailForContact, SomeTag


class InlineDetailForContact(admin.TabularInline):
    model = DetailForContact


class InlineDetailForTags(admin.TabularInline):
    model = Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = (InlineDetailForContact,)


@admin.register(SomeTag)
class TagsAdmin(admin.ModelAdmin):
    inlines = (InlineDetailForTags,)
