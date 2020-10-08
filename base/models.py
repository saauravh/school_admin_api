from django.db import models


class CommonFields(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)

    class Meta:
        abstract = True 








CLASS_CHOICES = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),)  #Create list with choices for class 1-12

class Teacher(CommonFields):
    
    class_assigned = models.CharField(max_length = 2,choices=CLASS_CHOICES)
    is_teacher = models.BooleanField(default=True, editable=False)
    
    def __str__(self):
        return self.first_name

class Student(CommonFields):
    class_present = models.CharField(max_length=2, choices=CLASS_CHOICES)
    is_student = models.BooleanField(default=True, editable=False)
    
    def __str__(self):
        return self.first_name
    
