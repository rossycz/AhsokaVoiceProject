from rest_framework import serializers
from LogroApp.models import logro 

class LogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = logro
        fields = '__all__'