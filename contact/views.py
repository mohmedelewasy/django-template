from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_message(request):

    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    context = {}
    return render(request, 'contact/contact.html', context)