from django.test import TestCase

# Create your tests here.
from api.models import Student, User, Course
from django.urls import reverse
#import http status code for code redability
from rest_framework import status

class StudentEnrollmentTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_superuser('user1', 'user@gmail.com', 'password1')
        user2 = User.objects.create(username='user2', password='password2')
        student1 = Student.objects.create(full_name='Sadiku Ajanaku', email='friday@gmail.com')
        student2 = Student.objects.create(full_name='Michael Faraday', email='michael@gmail.com')
        Course.objects.create(course_code='302', title='Advanced Calculus', credits='5', instructor='Dr. Akinbile Opeyemi')
        Course.objects.create(course_code='304', title='String Theory', credits='3', instructor='Dr. Abdullahi Adanavo')

    def test_get_student_info(self):
        # user = User.objects.get(username='user1', password='password1')
        self.client.login(username='user1', password='password1')
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_courses(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        courses = response.json()
        print(courses)