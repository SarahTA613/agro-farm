from django.urls import path
from .views import CustomerRegisterView

urlpatterns = [
    
    path("customer-register/",CustomerRegisterView.as_view(),name="customer-register"),
]