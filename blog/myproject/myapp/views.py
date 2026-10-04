from django.shortcuts import render
from myapp.models import Post

# Create your views here.
def show_posts(request):

    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts':posts})

def single_post(request, post_id):
    post = Post.objects.get(id = post_id)

    return render(request, 'posts/detalhes.html', {'post':post})