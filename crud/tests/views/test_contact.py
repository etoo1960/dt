from django.test import Client, TestCase

from crud.models.contact import Contact

class ContactTest(TestCase):
    
    def setUp(self):
        Contact.objects.create(name="Andrew Laurel", address="41 Bolton", telephone="09034893214")
        
    def test_index(self):
        client = Client()
        Contact.objects.create(name="Shehu Sani", address="88 Dean Road", telephone="090904859302")
        response = client.get("/crud/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["contacts"]), 2)
        
    def test_validate_telephone(self):
        client = Client()
        Contact.objects.create(name="Bill Mason", address="89 London Road", telephone="09076845362")
        response = client.get("/crud/validate_telephone/", {"telephone": "09076845362"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["is_taken"], True)
        
    def test_create(self):
        client = Client()
        response = client.post("/crud/create/", {"telephone": "09079409742", "name": "Anthony Jubois", "address": "21 California Street"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["telephone"], "09079409742")
        
    def test_delete(self):
        client = Client()
        contact = Contact.objects.create(name="Bill Mason", address="89 London Road", telephone="09076845362")
        response = client.get(f"/crud/delete/{contact.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["success"], "Contact successfully deleted")
        
    def test_show(self):
        client = Client()
        contact = Contact.objects.create(name="Elon Trump", address="89 Pentagon Road", telephone="09090347823")
        response = client.get(f"/crud/show/{contact.pk}/")
        self.assertEqual(response.status_code, 200)
        
    def test_update(self):
        client = Client()
        contact = Contact.objects.create(name="Bill Mason", address="89 London Road", telephone="09076845362")
        response = client.post(f"/crud/update/{contact.pk}/", {"telephone": "09079445784", "name": "Anthony Jubois", "address": "21 California Street"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["Successful"], "Contact Successfully Updated")