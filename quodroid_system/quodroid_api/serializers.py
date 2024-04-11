from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.ModelSerializer):
    
    steps = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    class Meta:
        model = Test
        fields = ["id", "title", "steps"]
