from django.urls import path

from .views import (HomepageView, ContactsListView, ContactDetailView,
                    CreateContact, UpdateContact, DeleteContact)

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('add-new-contact/', CreateContact.as_view(), name='add'),
    path('<uuid:pk>', ContactDetailView.as_view(), name='detail'),
    path('<pk>/delete/', DeleteContact.as_view(), name='delete'),
    path('<pk>/update/', UpdateContact.as_view(), name='update')
]
