from rest_framework import generics, permissions

from .serializers import TeacherSerializer, StudentSerializer
from .models import Teacher, Student
from .permissions import IsAdminOrIsTeacher


class TeacherList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentList(generics.ListCreateAPIView):
    #add custom permissions classes here
    permission_classes = (IsAdminOrIsTeacher,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    #add custom permissions classes here
    permission_classes = (IsAdminOrIsTeacher,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


