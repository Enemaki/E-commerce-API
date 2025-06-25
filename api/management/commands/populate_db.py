from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
from django.utils import lorem_ipsum
import random

from api.models import Student, Course, Enrollment, User

class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='test')
        
        students = [
            Student(full_name="Jane Doe", email="jane@example.com"),
            Student(full_name="John Smith", email="john@example.com")
        ]

        Student.objects.bulk_create(students)
        students = Student.objects.all()

        courses = [
            Course(course_code="CS101", title="Intro to Computer Science", credits=3, instructor="Dr. Ada"),
            Course(course_code="MATH201", title="Calculus I", credits=4, instructor="Dr. Newton")
        ]

        Course.objects.bulk_create(courses)
        courses = Course.objects.all()

        for item in range(len(students)):
            random_grade = ['A', 'B', 'C', 'D', 'E']
            Enrollment.objects.create(student=students[item], course=courses[item], grade=random.choice(random_grade))


