from django.shortcuts import render


def post_home(request):
	return render(request, 'post_home.html')