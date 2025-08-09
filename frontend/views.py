from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    # User submits the email form
    if request.method == 'POST':
        form = ContactForm(request.POST)

        # If form valid, clean the data for use
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Try to send the email (parameters: subject, body, from email, to email) 
            try:
                send_mail(
                    f"Contact Form: {subject}",
                    f"""
                    Name: {name}
                    Email: {email}
                    Subject: {subject}
                    Message: {message}
                    """,
                    settings.DEFAULT_FROM_EMAIL,
                    ['victoryma23@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message. We will reach out when possible.')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again.')
    # On initial page load, give the form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def resources(request):
    return render(request, 'resources.html')