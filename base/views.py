from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_subject = request.POST['message-subject']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            subject=message_subject,  # subject
            message=message,  # message
            from_email=message_email,  # from email
            recipient_list=['duresakorroso2019@gmail.com'],  # to email
        )
        return render(request, 'base/message.html', {'message_name': message_name})
    return render(request, 'base/home.html', {})
