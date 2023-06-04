
from django.shortcuts import render,redirect
from .models import StargEntertainment
# Create your views here.



def home (request):

    slims = StargEntertainment.objects.all()
    selftitle = ("What is your main goal when you make music")

    
    content={
        'slims':slims,
        'selftitle':selftitle,
    }
    return render(request, 'home.html',content)

def events (request):
    title = 'Slimstarg | Events'
    slims = StargEntertainment.objects.all()
    
    context = {
        'title':title,
        'slims':slims
    }
    return render(request,'events.html',context)

def tophit (request):
    
    return render(request,'tophit.html')

def admin (request):
    return render(request, 'admin.html',{})

def ack(request):
    title = "Your email was sent Successfully Chief"
    return render(request,'ack.html',{'title':title})

def contact (request):
    email = "email: slimofizzy@gmail.com"
    phone = 'phone: 08154240377'
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        return render(request,'home.html',{'message':"Your email was sent Successfully Chief"})

    else:
        context ={
            'email':email,
            'phone':phone
        }
            
        return render(request,'contact.html',context)
    
    
    
    