from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['duresakorroso2019@gmail.com'],  # to email
        )
        return render(request, 'base/message.html', {'message_name': message_name})
    return render(request, 'base/home.html', {})
