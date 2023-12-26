from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from .models import Contact

# Create your views here.
def index(request):
    data_list= Contact.objects.all()
    return render(request,"index.html",{'data':data_list})

def about(request):
    return render(request,"about.html")
    # return HttpResponse("This is my about page.")

def services(request):
    return render(request,"services.html")
    return HttpResponse("This is my servies page.")

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        text=request.POST.get('text')
        country=request.POST.get('country')
        contact=Contact(name=name, email=email, phone=phone,text=text,country=country, date=datetime.today())    
        contact.save()
        messages.success(request, "We got your credentials, We will contact you Shorlty.")
    return render(request,"contact.html")
    # return HttpResponse("This is my contact page.")

def newpage(request):
    return render(request, "newpage.html")