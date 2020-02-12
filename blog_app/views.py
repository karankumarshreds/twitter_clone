from django.shortcuts import render
from django.http import HttpResponse 

posts = [
	{'author': 'Karan Kumar',
	'content': 'This is the first blog post',
	'date': '2/11/2020',
	'title': 'Random title'},

	{'author': 'Jason Richardson',
	'content': 'This is the first blog post,This is the first blog post,This is the first blog post,This is the first blog post,This is the first blog post,This is the first blog post,This is the first blog post',
	'date': '3/11/2020',
	'title': 'random title'},
]

def home(request):
	context = {'posts': posts}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {})

