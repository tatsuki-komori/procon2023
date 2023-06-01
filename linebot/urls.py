from django.urls import path
from . import views

urlpatterns = [
    path('webhook/', line_webhook, name='line_webhook'),
]
