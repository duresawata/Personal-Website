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
        message_body = f"FROM: {message_email}\nName: {message_name}\n\n{message}"
        # send an email
        send_mail(
            subject=message_subject,  # subject
            message=message_body,  #
            from_email=message_email,  # from email
            recipient_list=['duresakorroso2019@gmail.com'],  # to email
        )
        context = {
            'message_name': message_name,
            'from_email': message_email,
            'subject': message_subject,
        }
        return render(request, 'base/message.html', context)
    return render(request, 'base/home.html', {})
