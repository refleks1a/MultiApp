from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import DeleteView
from notifications.views import DeleteNotification
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='main'),

    path('delete_notification/<int:id>/', DeleteNotification, name='delete_notification'),

    path('login/', CustomLogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='main:main'), name='logout'),
    path('signup/', CustomSignUpView.as_view(), name='signup'),
]