from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.show_all_contacts, name="show_all_contacts"),
    path("create_contact", views.create_contact, name="create_contact"),
    path("<int:pk>/", include([
        path('edit', views.edit, name='edit'),
        path('delete', views.delete, name='delete')
    ])),
]