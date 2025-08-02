from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.



def generic_api(model_class, serializer_class):
    @api_view(['GET','POST', 'DELETE', 'PUT'])
    # @permission_classes([IsAuthenticated])


    def api(request, id = None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many = True)
                return Response(serializer.data)

        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Success
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # If serializer is invalid


        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    instance.delete()
                    return Response({'message':'Delete Successfully'})
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
                

        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                    return Response(serializer.data)
                
                        
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    return api


manage_student = generic_api(Student, StudentSerialize)

manage_admin = generic_api(Admin, AdminSerializer)

manage_maintenance = generic_api(Maintenance, MaintenanceSerializer)

manage_suggestion = generic_api(Suggestion, SuggestionSerializer)\
    
    
    


class StudentLoginAPIView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data['student_id']
            password = serializer.validated_data['password']

            try:
                student = Student.objects.get(id=student_id)
                if student.password == password:
                    return Response({
                        'message': 'Login successful',
                        'student_id': student.id,
                        'name': student.name,
                        'email': student.email,
                        'phone': student.phone,
                        'department': student.department,
                    })
                else:
                    return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

class AdminLoginAPIView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['user_name']
            password = serializer.validated_data['password']

            try:
                admin = Admin.objects.get(id=user_name)
                if admin.password == password:
                    return Response({
                        'message': 'Login successful',
                        'user_name': admin.user_name,
                    })
                else:
                    return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Admin.DoesNotExist:
                return Response({'error': 'Admin not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    # new login
    # views.py


class AdminLoginView(APIView):
    def post(self, request):
        user_name = request.data.get('user_name')
        password = request.data.get('password')
        
        if not user_name or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            admin = Admin.objects.get(user_name=user_name)
        except admin.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Here you would check password hash, but let's do a simple check for demo
        if admin.password != password:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = AdminLoginSerializer(admin)
        return Response(serializer.data)


class StudentLoginView(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        password = request.data.get('password')
        
        if not student_id or not password:
            return Response({"error": "Student ID and password required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            student = Student.objects.get(student_id=student_id)
        except student.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Here you would check password hash, but let's do a simple check for demo
        if student.password != password:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = StudentLoginSerializer(student)
        return Response(serializer.data)

