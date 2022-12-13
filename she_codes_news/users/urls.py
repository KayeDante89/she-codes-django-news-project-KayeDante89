from django.urls import path
from .views import CreateAccountView, Profile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name ='createAccount'),
    path('<int:pk>/', Profile.as_view(), name='profile'),
]