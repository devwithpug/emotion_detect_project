from rest_framework import viewsets
from .serializers import FaceSerializer
from .models import Face
from rest_framework import permissions


class FaceView(viewsets.ModelViewSet):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save()
