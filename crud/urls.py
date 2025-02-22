from django.urls import path

from crud.views import contact

app_name = "crud"
urlpatterns = [
    path('', contact.index, name='index'),
    path('validate_telephone', contact.validate_telephone, name='validate_telephone'),
    path('create', contact.create, name='create'),
    path('delete/<pk>/', contact.delete, name='delete')
    # path('posts/<int:pk>/', post.index, name='post-detail'),
]