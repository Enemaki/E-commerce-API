from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    pass

class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

class Course(models.Model):
    course_code = models.CharField(max_length=50)
    title = models.TextField()
    credits = models.PositiveIntegerField()
    instructor = models.CharField(max_length=250)
    students = models.ManyToManyField(Student, through="enrollment", related_name='course')

    def __str__(self):
        return f"{self.course_code} titled {self.title}"
    
class Enrollment(models.Model):
    A='A' 
    B='B' 
    C='C' 
    D='D'
    E='E'
    GradeChoices = {
        A:'A', B:'B', C:'C', D:'D', E:'E'
    }
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True,
    blank=True)
    grade = models.CharField(
        max_length=2, 
        choices=GradeChoices, 
        default=C,
        null=True,
        blank=True
    )
    enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} enrolled for {self.course.course_id} on {self.enrolled}"