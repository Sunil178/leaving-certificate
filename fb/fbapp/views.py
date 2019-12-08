from django.shortcuts import render,redirect
from .models import User, Friend
from django.http import JsonResponse
# Create your views here.

def index(request):
	user = User.objects.all().exclude(id = request.session['user_id'])
	friend = Friend.objects.filter(user_id = request.session['user_id'])
	if friend:
		req_frd = friend[0].requested_frd.split(',')
		req_frd = list(map(int, req_frd))
		list_of_suggestions = []
		for person in user:
			if person.id not in req_frd:
				list_of_suggestions.append(person)
		return render(request, 'index.html', {'row': list_of_suggestions[::-1]})
	else:
		return render(request, 'index.html', {'row': user})

def viewRegister(request):
	return render(request, 'register.html')

def register(request, image):
	obj = User.objects.filter(email = request.POST['email'])
	if obj:
		return JsonResponse({'status': 1})
	user = User()
	user.name = request.POST['name']
	user.email = request.POST['email']
	user.password = request.POST['password']
	user.image = image
	user.save()
	user = User.objects.get(email = request.POST['email'])
	request.session['user_id'] = user.id
	return JsonResponse({'status' : 0})

def loginPage(request):
	return render(request, 'login.html', {'status': 0})

def checkLogin(request):
	user = User.objects.filter(email = request.POST['email'])
	if user:
		if user[0].password == request.POST['pwd']:
			request.session['user_id'] = user[0].id
			return redirect("/index/")
		else:
			return render(request, 'login.html', {'status': 1})
	else:
		return redirect('/')

def editProfile(request, id):
	obj = User.objects.get(id = id)
	print(obj)
	return render(request, 'editprofile.html', {'row':obj})

def profileUpdated(request, id):
	user = User.objects.get(id = id)
	user.name = request.POST['name']
	user.email = request.POST['email']
	user.save()
	return redirect("/index/")

def sendRequest(request, id):
	friend = Friend.objects.filter(user_id = id)
	if friend:
		reqfrd = friend[0].pending_frd.split(",")
		requested_friends =list(map(int,reqfrd))
		if request.session['user_id'] not in requested_friends:
			friend[0].pending_frd += "," + str(request.session['user_id'])
			friend[0].save()
	else:
		friend = Friend()
		friend.user_id = id
		friend.pending_frd = request.session['user_id']
		friend.save()
	friend = Friend.objects.filter(user_id = request.session['user_id'])
	if friend:
		reqfrd = friend[0].requested_frd.split(",")
		requested_friends = list(map(int, reqfrd))
		if id not in requested_friends:
			friend[0].requested_frd += ',' + str(id)
			friend[0].save()
	else:
		friend = Friend()
		friend.user_id = request.session['user_id']
		friend.requested_frd = id
		friend.save()
	return JsonResponse({'status': 'success'})

def showRequest(request):
	friend = Friend.objects.filter(user_id = str(request.session['user_id']))
	frd = friend[0].pending_frd
	frd = frd.split(",")
	print(frd)
	return redirect("/index/")

def myProfile(request):
	user = User.objects.get(id = request.session['user_id'])
	print(user)
	return render(request, 'myprofile.html', {'profile': user})

def pendingRequests(request):
	friend = Friend.objects.filter(user_id = request.session['user_id'])
	if friend:
		reqfrd = friend[0].pending_frd.split(",")
		requested_friends =list(map(int,reqfrd))
		lst = []
		for i in requested_friends:
			user = User.objects.get(id = i)
			lst.append(user)
		return render(request, "reqfrd.html", {'reqfriend':lst})

def acceptRequest(request, id):
	friend = Friend.objects.get(user_id = request.session['user_id'])
	reqfrd = friend.pending_frd.split(",")
	requested_friends = list(map(int, reqfrd))
	if id in requested_friends:
		requested_friends.remove(id)
		friend.frd += str(id) + ','
		requested_friends = list(map(str, requested_friends))
		friend.pending_frd = ",".join(requested_friends)
		friend.save()
		return redirect("/index/")


def requestedFriends(request):
	friend = Friend.objects.get(user_id = request.session['user_id'])
	req_frd = friend.requested_frd.split(',')
	list_of_frd = list(map(int, req_frd))
	list_of_row = []
	for i in list_of_frd:
		list_of_row.append(User.objects.get(id = i))
	return render(request, 'requested_friends.html', {'row': list_of_row})

