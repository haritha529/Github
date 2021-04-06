from django.shortcuts import render

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def login(request):
	return render(request,'html/login.html')

def register(request):
	if request.method=="POST":
		u=request.POST['username']
		p=request.POST['pas']
		m=request.POST['mal']
		a=request.POST['ag']
		d={'us':u,'em':m,'age':a,'ps':p}
		return render(request,'html/detail.html',{'d':d})
	return render(request,'html/register.html')
















	