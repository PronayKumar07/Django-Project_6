from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('about/', views.about, name = "aboutpage"),
    path('submitFrom/', views.submitFrom, name = "From"),
    # path('djangoform/', views.djangoform, name = 'From2')
    path('djangoform/', views.PasswordValidation, name = 'From2')
]