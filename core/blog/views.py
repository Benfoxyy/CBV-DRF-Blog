from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Post

class IndexView(ListView):
    queryset = Post.objects.all()
    paginate_by = 2

class SingleView(DetailView):
    model = Post

class CreatePost(CreateView):
    model = Post
    fields = ['title','content','category']
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = True
        return super().form_valid(form)
    