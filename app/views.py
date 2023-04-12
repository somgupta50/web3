from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
from .models import Contact
from .forms import ContactForm


# Create your views here.
def landing(request):
    return render(request, 'landing.html')


def feedback(request):
    feedform = FeedbackForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        rating = request.POST.get('rating')
        if len(name) > 0 and len(email) > 0 and len(message) > 0:
            feed = Feedback(name=name, email=email, message=message, rating=rating)
            feed.save()
            print('Feedback saved')
    ctx = {'form':feedform}
    return render(request, 'feedback.html', ctx)


def contact(request):
    contform = ContactForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        
        if len(name) > 0 and len(email) > 0 and len(subject) > 0:
            cont = Contact(name=name, email=email, subject=subject, mobile=mobile)
            cont.save()
            print('saved')
    ctx = {'form':contform}
    return render(request, 'contact.html', ctx)