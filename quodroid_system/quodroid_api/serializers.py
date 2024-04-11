from rest_framework import serializers
from .models import Test, Tests

class TestSerializer(serializers.ModelSerializer):
    
    steps = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    class Meta:
        model = Test
        fields = ["id", "title", "steps"]

class TestsSerializer(serializers.ModelSerializer):

    tests = TestSerializer(many=True)

    class Meta:
        model = Tests
        fields = ['tests']
    
    