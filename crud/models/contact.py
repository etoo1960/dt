from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    

    def __str__(self):
        return self.telephone

    def get_absolute_url(self):
        return reverse("crud:show", kwargs={"pk": self.pk})
