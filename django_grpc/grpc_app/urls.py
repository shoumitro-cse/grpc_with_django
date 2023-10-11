from django.urls import path
from . import views


urlpatterns = [
    path('send/', views.IOTReceiveAPIView.as_view()),
]
