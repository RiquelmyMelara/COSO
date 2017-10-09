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

    def get_queryset(self):
        """ allow rest api to filter by submissions """
        queryset = COSO.objects.all()
        nombreCoso = self.request.query_params.get('name', None)

        if nombreCoso is not None:
            queryset = queryset.filter(nombreCoso=nombreCoso)

        return queryset

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer

    def get_queryset(self):
        """ allow rest api to filter by submissions """
        queryset = Componente.objects.all()
        COSO = self.request.query_params.get('COSO', None)
        nombre = self.request.query_params.get('name', None)
        if COSO is not None:
            queryset = queryset.filter(COSO=COSO)
        if nombre is not None:
            queryset = queryset.filter(nombre=nombre)

        return queryset

class PrincipioViewSet(viewsets.ModelViewSet):
    queryset = Principio.objects.all()
    serializer_class = PrincipioSerializer

class EnfoqueViewSet(viewsets.ModelViewSet):
    queryset = Enfoque.objects.all()
    serializer_class = EnfoqueSerializer

class EnunciadosViewSet(viewsets.ModelViewSet):
    queryset = Enunciados.objects.all()
    serializer_class = EnunciadosSerializer
