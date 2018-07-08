from django.shortcuts import render

# Create your views here.
def signin(request):
	context = {}
	return render(request, 'signin.html', context)

def signup(request):
	context = {}
	return render(request, 'signup.html', context)
