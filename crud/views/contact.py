from django.shortcuts import render
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from django.http import JsonResponse
from django.core import serializers

from crud.forms.contact_form import ContactForm
from crud.models.contact import Contact


def index(request):
    contacts = Contact.objects.all()
    
    return render(request, 'crud/contact.html', {"contacts": contacts})

def validate_telephone(request):
    """Check username availability"""
    telephone = request.GET.get('telephone', None)
    response = {
        'is_taken': Contact.objects.filter(telephone__iexact=telephone).exists()
    }
    return JsonResponse(response)

@require_POST
def create(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data['telephone']
        form.save()
        return JsonResponse({"telephone": telephone}, status=200)
    else:
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)
    
def delete(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return JsonResponse({"success": "Contact successfully deleted"})
    except Contact.DoesNotExist:
        return JsonResponse({"error": "Contact does not exists"})
        
def show(request, pk):
    try:
        contact = Contact.objects.filter(pk=pk)
        data = serializers.serialize('json', contact, fields=["name", "telephone", "address"])
        return JsonResponse({"contact": data})
    except Contact.DoesNotExist:
        return JsonResponse({"error": "Contact does not exists"})

