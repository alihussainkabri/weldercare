from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import smtplib
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    title = "Home - Welldercare"
    news = New.objects.all().order_by("-id")[:3]
    return render(request,'welderapp/index.html',{"title" : title,"news" : news})

def whoWeAre(request):
    title = "Who We Are - Welldercare"
    return render(request,'welderapp/Who-We-Are.html',{"title" : title})

def whyChooseUs(request):
    title = "Why Choose Us"
    return render(request,'welderapp/Why-Choose-Us.html',{"title" : title})

def news(request):
    title = "News - Welldercare"
    news = New.objects.all().order_by("-id")
    category = Category.objects.all().order_by("-id")
    return render(request,'welderapp/news.html',{"title" : title,"news" : news,"categories" : category})

def newsByMonth(request,condition):
    category_id = condition.split("-")[1]
    category = Category.objects.filter(id=category_id)[0]
    title = "News - Welldercare"
    news = New.objects.filter(category=category).order_by("-id")
    category = Category.objects.all().order_by("-id")
    return render(request,'welderapp/news.html',{"title" : title,"news" : news,"categories" : category})

def contact(request):
    title = "Contact Us - Welldercare"
    return render(request,'welderapp/contact.html',{"title" : title,"value" : "0"})

def career(request):
    title = "Careers - Welldercare"
    carrers = Career.objects.all().order_by("-id")
    return render(request,'welderapp/career.html',{"title" : title,"carrers" : carrers,"value" : "0"})

def tnc(request):
    title = "Copyright Notice and Usage Information - Welldercare"
    return render(request,'welderapp/tnc.html',{"title" : title})

def privacyPolicy(request):
    title = "Privacy Policy - Welldercare"
    return render(request,'welderapp/Privacy-Policy.html',{"title" : title})

def contactPost(request):
    if (request.method == "POST"):
        email = request.POST['email']
        name = request.POST['name']
        mobile = request.POST['mobile']

        contact = Contact(name=name,email=email,mobile=str(mobile))
        contact.save()
        subject = 'Contact Request has been submitted'
        message = f"Contact Enquiry Created by Name :-  {name} \n email:- {email}\n mobile :- {mobile}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["Pratika@Welldercare.life", ]
        send_mail( subject, message, email_from, recipient_list )
        title = "Contact Us - Welldercare"
        return render(request,'welderapp/contact.html',{"title" : title,"value" : "1"})
    else:
        title = "Contact Us - Welldercare"
        return render(request,'welderapp/contact.html',{"title" : title,"value" : "0"})

def jobPost(request):
    if (request.method == "POST"):
        email = request.POST['email']
        name = request.POST['name']
        mobile = request.POST['mobile']
        file = request.FILES['file']

        job = JobApply(name=name,email=email,mobile=str(mobile),file=file)
        job.save()
        title = "Careers - Welldercare"
        carrers = Career.objects.all().order_by("-id")
        subject = 'Job Request has been submitted'
        message = f"Job Enquiry Created by Name :-  {name} \n email:- {email}\n mobile :- {mobile}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["careers@welldercare.life", ]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'welderapp/career.html',{"title" : title,"carrers" : carrers,"value" : "1"})
    else:
        title = "Careers - Welldercare"
        carrers = Career.objects.all().order_by("-id")
        return render(request,'welderapp/career.html',{"title" : title,"carrers" : carrers,"value" : "0"})
