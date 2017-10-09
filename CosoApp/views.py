from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from CosoApp.models import COSO, Componente, Principio, Enfoque, Enunciados, Enunciados
from CosoApp.serializers import UserSerializer, GroupSerializer, COSOSerializer, ComponenteSerializer, PrincipioSerializer, EnfoqueSerializer, EnunciadosSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class COSOViewSet(viewsets.ModelViewSet):
    queryset = COSO.objects.all()
    serializer_class = COSOSerializer

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = COSOSerializer

class PrincipioViewSet(viewsets.ModelViewSet):
    queryset = Principio.objects.all()
    serializer_class = PrincipioSerializer

class EnfoqueViewSet(viewsets.ModelViewSet):
    queryset = Enfoque.objects.all()
    serializer_class = EnfoqueSerializer

class EnunciadosViewSet(viewsets.ModelViewSet):
    queryset = Enunciados.objects.all()
    serializer_class = EnunciadosSerializer
