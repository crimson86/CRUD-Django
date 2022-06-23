from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView


# Create your views here.


class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__ all__"
    success_url  = reverse_lazy ("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__ all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__ all__"
    success_url  = reverse_lazy("blog:all")