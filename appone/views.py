
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
from smtplib import SMTPException
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

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
    return render(request, 'enginepics.html')


def handymanpics(request):
    return render(request, 'handymanpics.html')


def logisticpics(request):
    return render(request, 'logisticpics.html')