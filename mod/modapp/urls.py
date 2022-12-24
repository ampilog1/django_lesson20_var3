from modapp import views
from django.urls import path

app_name = 'modapp'

urlpatterns = [
    path('', views.main_view),
]