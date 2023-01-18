from userapp import views
from django.urls import path

app_name = 'userapp'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login')
]
