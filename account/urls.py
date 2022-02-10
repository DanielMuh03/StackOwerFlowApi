from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/', ActivateAPIView.as_view()),
]