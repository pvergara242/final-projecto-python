# from tags.serializer import TagsSerializer
from tags.models import Tag
from rest_framework import viewsets
from tags.serializer import  TagSerializer

# Create your views here.
class Tag(viewsets.ModelViewSet) :
    queryset = Tag.objects.all()
    serializer_class = TagSerializer