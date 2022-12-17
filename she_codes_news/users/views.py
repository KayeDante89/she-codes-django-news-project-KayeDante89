from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from news.models import NewsStory

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class EditAccountView(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    context_object_name = 'createAccount'
    template_name = 'users/createAccount.html'
    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.id})

class Profile(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk']).order_by('-pub_date')
        return context

    