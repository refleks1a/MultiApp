from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import DeleteView


from .views import *


urlpatterns = [
    path('', NotesList.as_view(), name='notes_list'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('sign_up/', CustomRegistrationView.as_view(), name='sign_up'),

    path('add_note/', NoteCreate.as_view(), name='add_note'),
    path('edit_note/<int:pk>/', NoteUpdate.as_view(), name='edit_note'),
    path('delete_note/<int:pk>/', NoteDelete.as_view(), name='delete_note'),
    path('view_note/<int:pk>/', NoteView.as_view(), name='view_note'),
]

