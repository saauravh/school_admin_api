from rest_framework import serializers


from .models import Teacher, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name', 'email', 'class_assigned',]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name','last_name', 'email', 'class_present',]

