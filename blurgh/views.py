from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
	published_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blurgh/post_list.html', {'published_posts': published_posts})

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blurgh/post_detail.html', {'post': post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', post_id=post.pk)
	else:
		form = PostForm()
	return render(request, 'blurgh/post_edit.html', {'form': form})

def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blurgh/post_edit.html', {'form': form})