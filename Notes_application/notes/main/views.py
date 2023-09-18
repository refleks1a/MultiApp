from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from .models import *


class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('notes_list')


class CustomRegistrationView(FormView):
    template_name = 'main/sign_up.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes_list')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(CustomRegistrationView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes_list')
        return super(CustomRegistrationView, self).get(*args, **kwargs)


class NotesList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'main/notes_list.html'
    context_object_name = 'notes'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['notes'] = context['notes'].filter(user=self.request.user)

        return context


class NoteView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'main/view_note.html'
    context_object_name = 'note'


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'main/add_note.html'
    success_url = reverse_lazy('notes_list')
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'main/edit_note.html'
    success_url = reverse_lazy('notes_list')
    fields = ['title', 'content']


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'main/delete_note.html'
    success_url = reverse_lazy('notes_list')
    context_object_name = 'note'
