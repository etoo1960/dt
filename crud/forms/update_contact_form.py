from django import forms

from crud.models.contact import Contact

class UpdateContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "telephone", "address", "id"]