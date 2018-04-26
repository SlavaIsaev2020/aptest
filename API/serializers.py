from rest_framework import  serializers
from .models import Student, Course
from rest_framework.relations import (  
    HyperlinkedIdentityField, HyperlinkedRelatedField, ManyRelatedField,
    PrimaryKeyRelatedField, RelatedField, SlugRelatedField, StringRelatedField,
)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'id', 'name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'lastName', 'courses', 'id','url')