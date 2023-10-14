from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, CreateView, ListView

from .models import Notification

@login_required
def DeleteNotification(request,id):

    notification = Notification.objects.get(id=id)
    notification.delete()

    return HttpResponseRedirect(redirect_to='/')


class CreateNotification(LoginRequiredMixin, CreateView):
    model = Notification
    template_name = 'notifications/create_notification.html'
    success_url = reverse_lazy('main:main')
    fields = ['title', 'content', 'expiry_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNotification, self).form_valid(form)


class NotificationsList(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notifications.html'
    context_object_name = 'notifications'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['notifications'] = Notification.objects.filter(user=self.request.user)

        return context


