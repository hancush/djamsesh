from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	published_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blurgh/post_list.html', {'published_posts': published_posts})

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blurgh/post_detail.html', {'post': post})