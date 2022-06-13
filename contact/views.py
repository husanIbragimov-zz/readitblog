from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactCreateForm


def contact_view(request):
    form = ContactCreateForm(request.POST or None)
    if form.is_valid():
        form .save()
        messages.success(request, 'Successfully send your message')
        return redirect('/contact/')
    return render(request, 'contact.html', {'form': form})
