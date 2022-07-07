from datetime import datetime
from django.shortcuts import render
from datetime import datetime
from projectApp.models import Contact
def home(request):
    return render(request,'index.html')

# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        phone=request.POST.get('phone')
        contact=Contact(name= name,email=mail,phone=phone,date=datetime.today())
        contact.save()
    return render(request,"contact.html")