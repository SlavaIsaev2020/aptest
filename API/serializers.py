from rest_framework import  serializers
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'id', 'name')

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class Meta:
        model = Student
        fields = ('name', 'courses', 'id','url')
    
    def create(self, validated_data):
        courses_data = validated_data.pop('courses')
        student = Student.objects.create(**validated_data)
        for course_data in courses_data:
            Course.objects.create(student=student, **course_data)
        return student