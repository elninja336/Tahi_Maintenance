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
    # Student_id = serializers.SlugRelatedField(
    #     queryset = Student.objects.all(),
    #     slug_field = 'Student_id'
    # )
    class Meta:
        model = Maintenance
        fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
    # Student_id = serializers.SlugRelatedField(
    #     queryset = Student.objects.all(),
    #     slug_field = 'Student_id'
    # )
    # student_name = serializers.CharField(source = 'Student.fullname', read_only=True)
    
    # student_name = serializers.SerializerMethodField()
    # dateField = serializers.DateTimeField(format="%d %B %Y, %I:%M %p")  # Example: 28 July 2025, 11:30 AM


    class Meta:
        model = Suggestion
        # fields = ['id', 'student_id','student_name', 'message', 'status', 'image', 'date']
        fields = '__all__'
        
    
        
        
# class StudentLoginSerializer(serializers.ModelSerializer):
#     student_id = serializers.CharField()
#     password = serializers.CharField()
    
    
    
# class AdminLoginSerializer(serializers.ModelSerializer):
#     user_name = serializers.CharField()
#     password = serializers.CharField()

# serializers.py

class AdminLoginSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Admin
        fields = ['id', 'user_name']
        
        
        
class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'fullname', 'email', 'student_id']
