from rest_framework import serializers
from .models import Job

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'