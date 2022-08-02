from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ContactsListView.as_view(), name="show_all_contacts"),
    path("create_contact", views.ContactCreateView.as_view(), name="create_contact"),
    path("<int:pk>/", include([
        path('edit', views.ContactUpdateView.as_view(), name='edit'),
        path('delete', views.ContactDeleteView.as_view(), name='delete')
    ])),
]