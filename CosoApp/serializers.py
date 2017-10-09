from django.contrib.auth.models import User, Group
from rest_framework import serializers
from CosoApp.models import COSO, Componente, Principio, Enfoque, Enunciados


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class COSOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COSO
        fields = '__all__'

class ComponenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'

class PrincipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Principio
        fields = '__all__'

class EnfoqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enfoque
        fields = '__all__'

class EnunciadosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enunciados
        fields = '__all__'
