from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()

    return render(request, 'blog/post_list.html', {'posts': posts, 'form': form})
