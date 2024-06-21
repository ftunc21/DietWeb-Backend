from rest_framework import generics
from .models import Diet
from .serializers import DietSerializer

class DietListCreate(generics.ListCreateAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
