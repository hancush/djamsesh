from django.shortcuts import render

def post_list(request):
	return render(request, 'blurgh/post_list.html', {})
