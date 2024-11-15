from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is varible in django"
    }
    
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage by pukhraj")

def about(request):
    # return HttpResponse("this is aboutpage by pukhraj")
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        item = request.POST.get('item')
        contact = Contacts(name=name, email=email, password=password, item=item)
        messages.success(request, "Contact has been saved !!!!")

        contact.save()


    return render(request, 'contact.html')

def home(request):
    # return HttpResponse("this is servicesss")
    return render(request, 'home.html')