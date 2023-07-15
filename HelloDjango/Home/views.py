from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from Home.models import Contacts
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable': "VARIABLE",
    }
   
    return render(request=request, template_name='index.html', context=context)
    # return HttpResponse('This is home page.')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is about me')


def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is services page')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('zip')
        desc = request.POST.get('desc')
        
        contact = Contacts(name=name, email=email, phoneno=phoneno, address=address, city=city, state=state, pin=pin, desc=desc, createdAt=datetime.today())

        contact.save()

        messages.success(request, "Response Submitted. Your Query will be addressed shortly.")

    return render(request, 'contacts.html')
    # return HttpResponse('This is contacts page')
