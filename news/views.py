from rest_framework import viewsets
from .serializers import NewSerializer
from .models import New

class NewViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewSerializer
    queryset = New.objects.all().order_by('-date')