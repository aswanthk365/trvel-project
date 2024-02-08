from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    service=servieces.objects.all()
    customer_feedback=customer_review.objects.all()
    return render(request,'index.html',{'ser':service,'cus_re':customer_feedback})

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')