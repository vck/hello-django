from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index_view(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		if title and content:
			post = Post(title=title, content=content)
			post.save()
			posts = Post.objects.all()
			return render(request, "index.html", {'posts': posts})
	posts = Post.objects.all()
	return render(request, "index.html", {'posts': posts})



