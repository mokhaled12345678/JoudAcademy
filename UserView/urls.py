from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('courses/', views.courses, name = 'courses'),
    path('faq/', views.faq, name = 'faq'),
    path('register/', views.register, name = 'register'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('course/<str:pk>/', views.course, name='course'),
    path('login/', views.login_user, name='login'),
    path('char/', views.char, name='char')
]