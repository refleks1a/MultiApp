from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from newsapi import NewsApiClient
from currentsapi import CurrentsAPI

from .models import *
from news.models import *
from notifications.models import *
import requests
import datetime
from django.utils import timezone
import geocoder


class CustomLogInView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main:main')


class CustomSignUpView(FormView):
    template_name = 'main/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(CustomSignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:main')
        return super(CustomSignUpView, self).get(*args, **kwargs)


def index(request):

    newsapi = CurrentsAPI(api_key='M4BI4JpSg3AwUPa10KeAHhH8ZUgagam2yNb90reGCP_-mQDZ')
    all__articles = newsapi.latest_news()['news']

    g = geocoder.ip('me')
    # weather_api_realtime = f"https://api.tomorrow.io/v4/weather/realtime?location={g.city}&apikey=QT7IoF5k8ORbklkycu9nxbLgn1u0Jkd0"
    # weather_api_forecast = f"https://api.tomorrow.io/v4/weather/forecast?location={g.city}&apikey=QT7IoF5k8ORbklkycu9nxbLgn1u0Jkd0"

    headers = {"accept": "application/json"}

    # response_realtime = requests.get(weather_api_realtime, headers=headers)
    # response_forecast = requests.get(weather_api_forecast, headers=headers)
    #
    # weather_forecast = (response_forecast.json()['timelines']['daily'][:5])

    weekly_data = {}
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # for j in range(5):
    #     if j == 0:
    #         weather_forecast[j]['values']['day_week'] = days_of_week[datetime.datetime.strptime(str(weather_forecast[j]['time'][:10]), '%Y-%m-%d').date().weekday()]
    #         daily_data = weather_forecast[j]['values']
    #     else:
    #         weekly_data[days_of_week[datetime.datetime.strptime(str(weather_forecast[j]['time'][:10]), '%Y-%m-%d').date().weekday()]] = weather_forecast[j]['values']['temperatureApparentAvg']

    notifications = []
    if request.user.is_authenticated:
        i = 0
        for notification in Notification.objects.filter(user=request.user):
            current_time = timezone.now()
            if notification.expiry_date <= current_time:
                notifications.append(notification)
                i += 1
            if i == 3:
                break

    context = {
        'news': News.objects.all(),
        # 'daily_data': daily_data,
        # 'weekly_data': weekly_data,
        'location': {'city': g.city, 'country': g.country},
        'notifications': notifications,
    }

    # News.objects.all().delete()
    # for i in range(4):
    #     News.objects.create(author=all__articles[i]['author'],
    #                         title=all__articles[i]['title'],
    #                         description=all__articles[i]['description'],
    #                         url=all__articles[i]['url'],
    #                         urlToImage=all__articles[i]['image'],
    #                         publishedAt=all__articles[i]['published'],
    #                         )

    return render(request, 'main/main.html', context=context)
