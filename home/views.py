from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
