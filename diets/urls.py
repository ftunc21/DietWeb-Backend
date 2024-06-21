from django.urls import path
from .views import DietListCreate

urlpatterns = [
    path('diets/', DietListCreate.as_view(), name='diet-list-create'),
]
