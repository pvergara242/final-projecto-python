from newsletters.serializer import NewslettersSerializer
from newsletters.models import Newsletter
from rest_framework import viewsets

# Create your views here.
class Newsletter(viewsets.ModelViewSet) :
    queryset = Newsletter.objects.all()
    serializer_class = NewslettersSerializer
