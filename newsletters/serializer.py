from rest_framework import serializers
from newsletters.models import Newsletter


class NewslettersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Newsletter
        fields='__all__'