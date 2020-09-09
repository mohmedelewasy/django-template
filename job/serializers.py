from rest_framework import serializers
from .models import Job, User
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'