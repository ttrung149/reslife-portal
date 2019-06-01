from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
)

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(PostListView.as_view()), name='home'),
    path('post/<int:pk>/', login_required(PostDetailView.as_view()),
         name='post-detail'),
]
