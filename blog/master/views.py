from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

def index_view(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		if title and content:
			post = Post(title=title, content=content)
			post.save()
			posts = Post.objects.all().order_by('upvote')
			return render(request, "index.html", {'posts': posts})
	posts = Post.objects.all().order_by('-id')
	return render(request, "index.html", {'posts': posts})


def view_page_id(request, post_id):
	try:
		post = Post.objects.get(id=post_id)
		return render(request, "page.html", {'post': post})
	except:
		return HttpResponseRedirect("/")
def delete_page_id(request, post_id):
	if request.method == "POST":
		try:
			post = Post.objects.get(id=post_id)
			print(post)
			post.delete()
			print('delete', post_id, 'success')
			return HttpResponseRedirect('/')
		except Exception as err:
			print(err)
			return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def upvote_post_id(request, post_id):
	if request.method == "POST":
		try:
			post = Post.objects.get(id=post_id)
			post.upvote += 1
			post.save()
			return HttpResponseRedirect('/')
		except:
			return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def downvote_post_id(request, post_id):
	if request.method == "POST":
		try:
			post = Post.objects.get(id=post_id)
			post.downvote += 1
			post.save()
			return HttpResponseRedirect('/')
		except:
			return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')


