from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView


from crud.models.contact import Contact


def index(request):
    contacts = Contact.objects.all()
    
    return render(request, 'crud/contact.html', {"contacts": contacts})
