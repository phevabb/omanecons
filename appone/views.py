
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
from smtplib import SMTPException

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from appone.models import *
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

            try:
                mail = EmailMessage(
                    subject=subject,
                    body=full_message,
                    from_email="phevab1@gmail.com",  # must match EMAIL_HOST_USER
                    to=["support@kkagroup.com"],
                    reply_to=[email],
                )
                mail.send(fail_silently=False)
                messages.success(request, "Your message has been sent successfully!")
                return redirect('contact')

            except BadHeaderError:
                messages.error(request, "Invalid header found. Please try again.")
            except SMTPException as e:
                messages.error(request, f"Email failed to send: {str(e)}")
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {str(e)}")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def logistics(request):
    return render(request, 'logistic.html')

def engine(request):
    return render(request, 'engine.html')

def handyman(request):
    return render(request, 'handyman.html')


def index2(request):
    return render(request, 'index2.html')





def enginepics(request):
    total_pics=Engine.objects.all()
    paginator_first_6 = Paginator(total_pics, 6)
    page = request.GET.get("page", 1)
    paged_pics = paginator_first_6.get_page(page)
    number_of_pics = total_pics.count()
    context = {"number_of_pics": number_of_pics, "total_pics": paged_pics,}
    return render(request, 'enginepics.html', context)



def handymanpics(request):
    total_pics=Handyman.objects.all()
    paginator_first_6 = Paginator(total_pics, 6)
    page = request.GET.get("page", 1)
    paged_pics = paginator_first_6.get_page(page)
    number_of_pics = total_pics.count()
    context = {"number_of_pics": number_of_pics, "total_pics": paged_pics,}
    return render(request, 'handymanpics.html', context)




def logisticpics(request):
    total_pics=Logistic.objects.all()
    paginator_first_6 = Paginator(total_pics, 6)
    page = request.GET.get("page", 1)
    paged_pics = paginator_first_6.get_page(page)
    number_of_pics = total_pics.count()
    context = {"number_of_pics": number_of_pics, "total_pics": paged_pics,}
    return render(request, 'logisticpics.html', context)
