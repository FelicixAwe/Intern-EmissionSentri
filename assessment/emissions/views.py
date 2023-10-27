from .models import Emission
from rest_framework import viewsets, permissions
from .serializers import EmissionSerializer


class EmissionListView(viewsets.ModelViewSet):
    queryset = Emission.objects.all()
    serializer_class = EmissionSerializer
    permission_classes = [permissions.IsAdminUser]
