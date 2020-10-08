from django.urls import path

from .views import TeacherList, TeacherDetail, StudentList,StudentDetail


urlpatterns = [
    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:pk>/', TeacherDetail.as_view()),
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
    

]