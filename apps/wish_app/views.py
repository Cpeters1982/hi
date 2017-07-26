from django.shortcuts import render,redirect
from models import Wish
from ..login_app.models import User
from django.contrib import messages

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)
# Create your views here.
def checkUser(request):
	try:
		if request.session['f_name'] < 2:
			return False
		else:
			return True
	except:
		return False

def index(request):
	# User.objects.all().delete()
	# Wish.objects.all().delete()


	results = checkUser(request)
	if results == False:
		return redirect('/')
	context = {
	'wishs': Wish.objects.all()
	}

	return render( request, 'wish_app/index.html', context)

def addForm(request):
	results = checkUser(request)
	if results == False:
		return redirect('/')
	return render( request, 'wish_app/addForm.html')
def addWish(request):
	results = checkUser(request)
	if results == False:
		return redirect('/')

	results = Wish.objects.createWish(request.POST)
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/wish/addform')
	else:
		messages.success(request, 'New item added!')
	return redirect('/wish')
