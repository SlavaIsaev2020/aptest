from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Course
from .serializers import CourseSerializer, StudentSerializer

# Create your views here.

# ViewSets define the view behavior.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer