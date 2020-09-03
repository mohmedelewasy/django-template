from django.shortcuts import render

# Create your views here.
def send_message(request):

    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

        print(message, name, email, subject)
    context = {}
    return render(request, 'contact/contact.html', context)