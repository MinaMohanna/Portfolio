from django.shortcuts import render
from .form import ContactForm

# Create your views here.

def contact(request):

    form = ContactForm()

    return render(request, 'contact/contact.html', {

        'form': form})
