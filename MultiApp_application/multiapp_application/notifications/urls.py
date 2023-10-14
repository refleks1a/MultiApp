from django.urls import path
from .views import CreateNotification, NotificationsList


app_name = 'notifications'

urlpatterns = [
    path('create_notification/', CreateNotification.as_view(), name='create_notification'),
    path('all_notification/', NotificationsList.as_view(), name='all_notification'),
]