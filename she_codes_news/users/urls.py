from django.urls import path
from .views import CreateAccountView, Profile, EditAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name ='createAccount'),
    path('<int:pk>/', Profile.as_view(), name='profile'),
    path('<int:pk>/edit', EditAccountView.as_view(), name="editAccount",)
]