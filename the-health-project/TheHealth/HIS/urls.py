from django.urls import path
from .views import home, adminLogin, createID

urlpatterns = [
    path('', home, name='home'),
    path('admin-login', adminLogin, name='admin-login'),
    path('create-id', createID, name='create-id'),
]
