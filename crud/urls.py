from django.urls import path

from crud.views import contact

app_name = "crud"
urlpatterns = [
    path('', contact.index, name='index'),
    # path('posts/<int:pk>/', post.index, name='post-detail'),
]