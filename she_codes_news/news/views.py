from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import NewsStory
from .forms import StoryForm, CommentForm
from django.contrib.auth import get_user_model




class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class AllStoriesView(generic.ListView):
    template_name = 'news/allStories.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditStoryView(generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def get_success_url(self):
        return reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "news/createComment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)
    
    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')
    
    

    

    

    
    
    


