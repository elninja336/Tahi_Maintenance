from rest_framework import serializers
from .models import *

class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        queryset = Student.objects.all(),
        slug_field = 'email'
    )
    class Meta:
        model = Maintenance
        fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        queryset = Student.objects.all(),
        slug_field = 'email'
    )

    class Meta:
        model = Suggestion
        fields = '__all__'