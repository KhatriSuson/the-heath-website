from django.urls import path
from .views import home, adminLogin, createID, index

urlpatterns = [
    path('', index, name='index'),
    path('admin-login', adminLogin, name='admin-login'),  
    path('create-id', createID, name='create-id'),
]
