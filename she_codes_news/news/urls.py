from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('all-stories/', views.AllStoriesView.as_view(), name="allStories"),
    path('<int:pk>/edit-story/', views.EditStoryView.as_view(), name="editStory"),
    path('<int:pk>/comment/', views.AddCommentView.as_view(), name="addComment"),
    path('author/<int:pk>/stories', views.AuthorStories.as_view(), name='authorstories'),
    path('<int:pk>/delete/', views.DeleteStoryView.as_view(), name="deleteStory"),
    path('<int:pk>/edit-comment/', views.EditCommentView.as_view(), name="editComment"),
    path('<int:pk>/delete-comment', views.DeleteCommentView.as_view(), name="deleteComment")
]
