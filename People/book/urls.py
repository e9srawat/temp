from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('login',views.login_user, name = 'login'),
    path('register',views.register, name = 'register'),
    path('dash',views.dash, name = 'dash'),
    path('logout', views.log_user, name='logout'), 
    path('create_contact/', views.create_contact, name='create_contact'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('get_contact_details/', views.get_contact_details, name='get_contact_details'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]


