from rest_framework import  viewsets
from usuarios.model import Usuario
from usuarios.serializer import Usuarios


# Create your views here.
class Usuario(viewsets.ModelViewSet) :
    queryset = Usuario.objects.all()
    serializer_class = Usuario.serializer
