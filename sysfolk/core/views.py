from rest_framework import permissions
from rest_framework import viewsets

from sysfolk.core.models import Person
from sysfolk.core.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.DjangoModelPermissions,)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.DjangoModelPermissions,)