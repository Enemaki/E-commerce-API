from rest_framework import serializers
from .models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'student_id',
            'full_name',
            'email',
            'enrollment_date'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'course_code',
            'title',
            'credits',
            'instructor',
        )

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = (
            'user',
            'student',
            'course',
            'grade',
            'enrolled'
        )