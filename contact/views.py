from django.shortcuts import render
from .form import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form
    })